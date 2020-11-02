#!/usr/bin/env python

import sys
import os
import json

sys.path.insert(0, 'src')

from etl import get_data
from features import get_features, clean_features
from stat_model import ttest


def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'features', 'model'.

    `main` runs the targets in order of data=>analysis=>model.
    '''

    if 'data' in targets:
        with open('config/data_params.json') as fh:
            data_cfg = json.load(fh)

        datafile = get_data(**data_cfg)

    if 'features' in targets:
        with open('config/features_params.json') as fh:
            feats_cfg = json.load(fh)

        data = get_features(datafile, feats_cfg)
        cleaned_data = clean_features(data)

    if 'model' in targets:
        with open('config/model_params.json') as fh:
            feats_cfg = json.load(fh)
        s, pval = ttest(cleaned_data, **feats_cfg)

    return

if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)
