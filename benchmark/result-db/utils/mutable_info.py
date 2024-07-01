def mutable_job_datatypes():
    return {
        'movie_companies': {
            'movie_id': 'INT NOT NULL',
            'note': 'CHAR 208',
        },
        'title': {
            'id': 'INT NOT NULL',
            'title': 'CHAR 334 NOT NULL',
            'production_year': 'INT',
        },
        'movie_info_idx': {
            'info': 'CHAR 10 NOT NULL',
            'movie_id': 'INT NOT NULL'
        },
        'keyword': {
            'id': 'INT NOT NULL',
            'keyword': 'CHAR 74 NOT NULL',
        },
        'name': {
            'id': 'INT NOT NULL',
            'name': 'CHAR 106 NOT NULL',
        },
        'aka_name': {
            'name': 'CHAR 218 NOT NULL',
            'person_id': 'INT NOT NULL',
        },
        'char_name': {
            'id': 'INT NOT NULL',
            'name': 'CHAR 478 NOT NULL',
        },
        'movie_info': {
            'info': 'CHAR 43 NOT NULL',
            'movie_id': 'INT NOT NULL',
        },
        'movie_keyword': {
            'movie_id': 'INT NOT NULL',
            'keyword_id': 'INT NOT NULL',
        },
        'cast_info': {
            'person_id': 'INT NOT NULL',
            'movie_id': 'INT NOT NULL',
            'person_role_id': 'INT',
        }
    }

def mutable_star_datatypes():
    return {
        'fact': {
            'id': 'INT NOT NULL',
            'fkd1': 'INT NOT NULL',
            'fkd2': 'INT NOT NULL',
            'fkd3': 'INT NOT NULL',
            'fkd4': 'INT NOT NULL',
            'a': 'INT NOT NULL',
            'b': 'CHAR 16 NOT NULL',
        },
        'dim1': {
            'id': 'INT NOT NULL',
            'a': 'INT NOT NULL',
            'b': 'CHAR 16 NOT NULL',
        },
        'dim2': {
            'id': 'INT NOT NULL',
            'a': 'INT NOT NULL',
            'b': 'CHAR 16 NOT NULL',
        },
        'dim3': {
            'id': 'INT NOT NULL',
            'a': 'INT NOT NULL',
            'b': 'CHAR 16 NOT NULL',
        },
        'dim4': {
            'id': 'INT NOT NULL',
            'a': 'INT NOT NULL',
            'b': 'CHAR 16 NOT NULL',
        },
    }