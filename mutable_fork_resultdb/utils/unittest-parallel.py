#!/usr/bin/env python3

import argparse
import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
import itertools
from enum import Enum
from tqdm import tqdm

class ReturnCode(Enum):
    SUCCESS = 0
    FAILURE = 1
    TIMEOUT = 2
    UNKNOWN = 3

def classify_returncode(returncode: int) -> ReturnCode:
    match returncode:
        case 0:
            return ReturnCode.SUCCESS
        case 1:
            return ReturnCode.FAILURE
        case 124 | 137:
            return ReturnCode.TIMEOUT
        case _:
            return ReturnCode.UNKNOWN

# data needed for junit output
class JunitData:
    errors = 0
    failures = 0
    tests = 0
    execution_time = 0.0
    test_cases = []

    def append_data(self, stdout: str, stderr: str, returncode: int, test_name: str):
        return_class = classify_returncode(returncode)

        # If a process times out we do not want to parse the result. It is just a failure.
        if return_class not in [ReturnCode.SUCCESS, ReturnCode.FAILURE]:
            self.errors += 1
            return

        assert stdout is not None
        tree = ET.fromstring(stdout)
        test_suite = tree.find('testsuite')
        assert test_suite is not None
        self.errors += int(test_suite.attrib['errors'])
        self.failures += int(test_suite.attrib['failures'])
        self.tests += int(test_suite.attrib['tests'])
        self.test_cases.append(test_suite.findall('testcase'))

    def dump(self, out: str):
        result = ET.Element('testsuites')
        result_child = ET.SubElement(result, 'testsuite')
        result_child.attrib['errors'] = str(self.errors)
        result_child.attrib['failures'] = str(self.failures)
        result_child.attrib['tests'] = str(self.tests)
        result_child.attrib['time'] = str(self.execution_time)
        for test_case in self.test_cases:
            result_child.extend(test_case)
        result_xml = ET.ElementTree(result)
        if out:
            result_xml.write(out)
        else:
            result_xml.write(sys.stdout.buffer)

    def is_failure(self):
        return self.errors > 0 or self.failures > 0


# data needed for human readable output
class TestData:
    total_assertions = 0
    passed_assertions = 0
    failed_assertions = 0

    total_test_cases = 0
    passed_test_cases = 0
    failed_test_cases = 0

    execution_time = 0.0

    error_msgs = []
    timeouted_tests = []
    unknown_test_failures = []
    has_test_failure = False

    def append_data(self, stdout: str, stderr: str, returncode: int, test_name: str):
        return_class = classify_returncode(returncode)

        # If a process times out we do not want to parse the result. It is just a failure.
        if return_class == ReturnCode.TIMEOUT:
            self.total_test_cases += 1
            self.failed_test_cases += 1
            self.has_test_failure = True
            self.timeouted_tests.append(test_name)
            return

        # If a process fails enexpectedly, we do not want to parse the result
        if return_class == ReturnCode.UNKNOWN:
            self.total_test_cases += 1
            self.failed_test_cases += 1
            self.has_test_failure = True
            self.unknown_test_failures.append((test_name, returncode))
            return

        current_failed_tests = 0
        assert stdout is not None
        assert stderr is not None

        # first match pattern
        match = re.search(r'All tests passed \((\d+) assertions? in (\d+) test case', stdout)
        if match:
            num_assertions = int(match.group(1))
            num_test_cases = int(match.group(2))

            self.total_assertions += num_assertions
            self.passed_assertions += num_assertions

            self.total_test_cases += num_test_cases
            self.passed_test_cases += num_test_cases
        else:
            match2 = re.search(
                r'test cases:\s*(?P<total>\d+)( \|\s*(?P<passed>\d+) passed)?( \|\s*(?P<failed>\d+) failed)?\nassertions:(\s*(?P<a_total>\d+)( \|\s*(?P<a_passed>\d+) passed)?( \|\s*(?P<a_failed>\d+) failed)?)?',
                stdout
            )
            if match2:
                self.total_assertions += int(match2.group('a_total')) if match2.group('a_total') is not None else 0
                self.passed_assertions += int(match2.group('a_passed')) if match2.group('a_passed') is not None else 0
                self.failed_assertions += int(match2.group('a_failed')) if match2.group('a_failed')  is not None else 0

                self.total_test_cases += int(match2.group('total'))
                self.passed_test_cases += int(match2.group('passed')) if match2.group('passed') is not None else 0
                current_failed_tests = int(match2.group('failed')) if match2.group('failed')  is not None else 0
                self.failed_test_cases += current_failed_tests
            else:
                tqdm.write(f'\u001b[31;1mFailed to match output of:\u001b[39;0m')
                tqdm.write(stdout)

        if current_failed_tests > 0:
            self.error_msgs.append(stdout)
            self.error_msgs.append(stderr)
            self.has_test_failure = True
        elif stderr != '':
            self.error_msgs.append(stderr)

    def dump(self, _):
        for msg in self.error_msgs:
            print(msg)

        if self.has_test_failure:
            digits_total = max(len(str(self.total_assertions)), len(str(self.total_test_cases)))
            digits_passed = max(len(str(self.passed_assertions)), len(str(self.passed_test_cases)))
            digits_failed = max(len(str(self.failed_assertions)), len(str(self.failed_test_cases)))
            print(f'\u001b[31;1m===============================================================================\u001b[39;0m')
            print(f'test cases: {self.total_test_cases:>{digits_total}} | \u001b[32;1m{self.passed_test_cases:>{digits_passed}} passed\u001b[39;0m | \u001b[31;1m{self.failed_test_cases:>{digits_failed}} failed\u001b[39;0m')
            print(f'assertions: {self.total_assertions:>{digits_total}} | \u001b[32;1m{self.passed_assertions:>{digits_passed}} passed\u001b[39;0m | \u001b[31;1m{self.failed_assertions:>{digits_failed}} failed\u001b[39;0m')

            if len(self.timeouted_tests) > 0:
                print(f'\n\u001b[31;1mTimeouts: {len(self.timeouted_tests)}\u001b[39;0m')
                print('\n'.join(map(lambda test: f'    {test}', self.timeouted_tests)))

            if len(self.unknown_test_failures) > 0:
                print(f'\n\u001b[31;1mUnknown test failures: {len(self.unknown_test_failures)}\u001b[39;0m')
                print('\n'.join(itertools.starmap(lambda test, ret: f'    {test} (return code {ret})', self.unknown_test_failures)))
        else:
            print(f'\u001b[32;1m===============================================================================\u001b[39;0m')
            print(f'\u001b[32;1mAll tests passed\u001b[39;0m ({self.passed_assertions} assertions in {self.passed_test_cases} test cases)\n')

        print(f'\nExecution time: {self.execution_time}s')

    def is_failure(self):
        if self.failed_assertions > 0 or self.failed_test_cases > 0:
            return True
        else:
            return False


def run_tests(args, test_names: list[str], binary_path: str, is_interactive: bool):
    # data used for output later
    data = JunitData() if args.report_junit else TestData()
    # max number of jobs as potentially specified by the user
    max_processes = args.jobs

    # used for --stop-fail
    failed = False

    progress_bar = tqdm(total=len(test_names), position=0, ncols=80, leave=False, bar_format='|{bar}| {n}/{total}', disable=(not is_interactive))

    command = ['timeout', '--signal=TERM', '--kill-after=' + str(args.timeout + 2), str(args.timeout), binary_path]
    if (args.report_junit):
        command += ['-r', 'junit']

    # we need to take the execution time by hand because the sum of all
    # junits is vastly inaccurate
    time_start = time.time()

    def handle_returncode(stdout: str, stderr: str, returncode: int, test_name: str):
        match returncode:
            # no error
            case 0 | 1:
                data.append_data(stdout, stderr, ReturnCode.NONE, test_name)

            # timout with SIGTERM or SIGKILL
            case 124 | 137:
                data.append_data(stdout, stderr, ReturnCode.TIMEOUT, test_name)

            # unexpected return code
            case _:
                data.append_data(stdout, stderr, ReturnCode.UNEXPECTED_RETURN, test_name)

    running_processes: map(int, tuple(subprocess.Popen, str)) = {}

    def wait_for_child() -> int:
        pid, status = os.wait()  # wait for *any* child to exit

        assert pid in running_processes, 'os.wait() returned unexpected child PID'

        process, p_test_name = running_processes[pid]
        assert process.pid == pid, 'PID mismatch'

        returncode = os.waitstatus_to_exitcode(status)  # get return status from process; don't use Popen.returncode
        assert returncode is not None

        progress_bar.update(1)
        del running_processes[pid]
        stdout, stderr = process.communicate()

        data.append_data(stdout, stderr, returncode, test_name)

        return returncode

    # execute tests in parallel until we have max_processes running
    for test_name in test_names:
        test_name = test_name.replace(',', '\\,')
        test_name = f'"{test_name}"'
        process = subprocess.Popen(command + [test_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        running_processes[process.pid] = (process, test_name)

        # if we have max_processes number of processes running, wait for a process to finish and remove the process from
        # the running processes dictionary
        if len(running_processes) >= max_processes:
            returncode = wait_for_child()
            if args.stop_fail and returncode != 0:  # stop on first failure
                failed = True
                break

    # wait for the remaining running processes to finish
    while len(running_processes) != 0:
        returncode = wait_for_child()
        if args.stop_fail and returncode != 0:  # stop on first failure
            failed = True
            break

    #  for pid, (process, p_test_name) in running_processes.items():
    #      stdout, stderr = process.communicate()  # wait for process to terminate; consume stdout/stderr to avoid deadlock
    #      progress_bar.update(1)
    #      handle_returncode(stdout, stderr, process.returncode, p_test_name)
    #      if process.returncode != 0 and args.stop_fail:
    #          failed = True
    #          break

    if failed:
        # send SIGTERM to all processes
        for process, test_name in running_processes.values():
            process.terminate()
        # wait 10ms for processes to terminate
        time.sleep(.01)
        # send SIGKILL if process did not terminate in time
        for process, test_name in running_processes.values():
            try:
                process.communicate()  # consume stdout/stderr to avoid deadlock
            except subprocess.TimeoutExpired:
                process.kill()

    progress_bar.close()
    time_end = time.time()
    execution_time = time_end - time_start
    data.execution_time = execution_time

    return data, failed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Run unittests on mutable. Note that the
                                                    unittest binary is assumed to be build/debug/bin/unittest.""")
    parser.add_argument('-j', '--jobs', help='Run N jobs in parallel. Defaults to number of CPU threads - 1.',
                        default=(os.cpu_count() - 1), metavar='N', type=int)
    parser.add_argument('-r', '--report-junit', help='Print the results in a junit report.', action='store_true')
    parser.add_argument('-s', '--stop-fail', help='Stop execution of tests on failure.', action='store_true')
    parser.add_argument('--timeout', help='Specify the timeout in seconds for each testcase. Defaults to 120 seconds',
                        default=120, metavar='TIMEOUT', type=int)
    parser.add_argument('-o', '--out', help='Path to output file (only for junit reports). Defaults to stdout.',
                        metavar='PATH', type=str)
    parser.add_argument('-t', '--tag', help='The tag of the tests to run. Defaults to [core] (only required tests).',
                        default='[core]', metavar='TAG', type=str)
    parser.add_argument('binary_path', help='Path to the unittest binary. Defaults to \'build/debug/bin/unittest\'.',
                        default=os.path.join('build', 'debug', 'bin', 'unittest'), type=str, metavar='PATH', nargs='?')
    args = parser.parse_args()

    # check if executable
    if not (os.path.isfile(args.binary_path) and os.access(args.binary_path, os.X_OK)):
        raise ValueError("Not a valid path to an executable.")

    # Check if interactive terminal
    is_interactive = True if 'TERM' in os.environ else False

    # get all the test names
    list_tests_command = [args.binary_path, '--list-test-names-only', '--order', 'rand', '--rng-seed', 'time', args.tag]
    output = subprocess.run(list_tests_command, stdout=subprocess.PIPE)
    test_names = output.stdout.decode().strip().split('\n')

    data, failed = run_tests(args, test_names, args.binary_path, is_interactive)

    data.dump(args.out)
    if failed or data.is_failure():
        exit(1)
    else:
        exit(0)

