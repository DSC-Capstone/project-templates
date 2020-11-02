
import pandas as pd

# Custom Features

def engine_size(df):
    
    return df['ENGINESIZE']

def cylinders(df):
    
    return df['CYLINDERS']


# putting features together


def feature_map():

    fmap = {
        "engine_size": engine_size,
        "cylinders": cylinders,
    }

    return fmap


def apply_features(df, feats, outfile=None):

    labels = df[['CO2EMISSIONS']]
    
    features = pd.DataFrame()
    fmap = feature_map()
    for feat in feats:
        f = fmap.get(feat)
        if f is not None:
            # custom feature found
            features[feat] = f(df)
        else:
            # feature is existing column
            features[feat] = df[feat]

    if outfile:
        features.to_csv(outfile, index=False)

    return features, labels

    

