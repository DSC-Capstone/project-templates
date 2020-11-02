#!/usr/bin/env python

import sys
import json

sys.path.insert(0, 'src')

from etl import get_data, load_training_data, load_test_data
from model import train


def main(targets):
    '''
        Runs the main project pipeline logic, given the targets.
        targets must contain: 'data', 'model'.

        `main` runs the targets in order of data=>model.
    '''


    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        get_data(data_cfg)
        train_images, train_labels = load_training_data(data_cfg["outdir"])
        test_images, test_labels = load_test_data(data_cfg["outdir"])
        data = (train_images, train_labels, test_images, test_labels)

    if 'model' in targets:
        print("in run -> model")
        with open('config/model-params.json') as fh:
            model_cfg = json.load(fh)

        train(data, model_cfg)



if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
