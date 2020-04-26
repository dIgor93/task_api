import os


def get_config():
    res = {}
    if os.environ.get('ENV') == 'PROD':
        res.update({'origin': 'https://task-tracker-heroku.herokuapp.com'})

    elif os.environ.get('ENV') == 'TEST':
        res.update({'origin': 'http://localhost:8080'})

    else:
        res.update({'origin': 'https://task-tracker-heroku.herokuapp.com'})

    return res


config = get_config()
