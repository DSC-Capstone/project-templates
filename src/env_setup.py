

import os
import json


basedir = os.path.dirname(__file__)
cred_fp = os.path.join(basedir, '..', '.env', 'kaggle.json')


def auth():
    '''
    set-up secrets for authentication to kaggle
    '''
    creds = json.load(open(cred_fp))

    os.environ['KAGGLE_KEY'] = creds.get('key')
    os.environ['KAGGLE_USERNAME'] = creds.get('username')

    return


def make_datadir():

    data_loc = os.path.join(basedir, '..', 'data')

    for d in ['raw', 'temp', 'out']:
        os.makedirs(os.path.join(data_loc, d), exist_ok=True)

    return
