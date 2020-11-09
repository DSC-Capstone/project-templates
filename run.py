

import sys
import json
import pandas as pd

sys.path.insert(0, 'src')
from etl import generate_data, save_data
from eda import generate_stats
from utils import convert_notebook



def main(targets):

    data_config = json.load(open('config/data-params.json'))
    eda_config = json.load(open('config/eda-params.json'))

    if 'data' in targets:

        data = generate_data(**data_config)
        save_data(data, **data_config)

    if 'eda' in targets:

        try:
            data
        except NameError:
            data = pd.read_csv(data_config['data_fp'])

        generate_stats(data, **eda_config)
        
        # execute notebook / convert to html
        convert_notebook(**eda_config)


if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)
