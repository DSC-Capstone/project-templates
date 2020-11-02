import pandas as pd
from collections import defaultdict

def feature_map():
    '''
    This function creates a feature map
    '''

    fmap = {
        "int": int,
        "float": float,
    }

    return fmap

def get_features(outdir, fields):
    '''
    This function creates a dataframe from the input data file.
    :param: outdir: input data data file
    :param: fields: a schema to create the columns of the dataframe
    '''

    inputfile = open(outdir,'r')
    table = defaultdict(list)
    fmap = feature_map()

    for line in inputfile.readlines():
        for f in fields.keys():
            try:
                raw_val = line[fields[f]["start"]-1:fields[f]["end"]]
                cast = fmap[fields[f]["type"]]
                val = cast(raw_val)
            except ValueError:
                val = None
            table[f].append(val)
    df = pd.DataFrame(data=table)

    return df

def clean_features(df):
    '''
    This function removes the records where the weight of the new born baby is
    greater than 20 lbs and also removes the rows where the outcome is other than
    1 which refers to dead new borns of different kinds. Creates a new column weight.
    :param: df: input dataframe
    '''

    df = df[(df['birthwgt_lb']<20) & (df['outcome']==1)].copy()
    df.loc[:, 'weight'] = df.apply(lambda row: row['birthwgt_lb']+ row['birthwgt_oz']/16, axis=1)
    df.to_csv("data/temp/cleaned_features.csv", index=False)
    
    return df
