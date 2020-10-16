#!/usr/bin/env python
#imports and runs library code on the parameters that you care by
#allow users to run this code without having to dig into the code
#unpacks key,value pair

import sys
import json

from etl import get_data

def main(targets):
    if "data" in targets:
        with open('data-params.json') as fh:
            data_cfg = json.load(fh)
        #make the data target
        get_data(**data_cfg)
    return
    if __name__ == '__main__':
        targets=sys.argv[1:]
        main(targets)
