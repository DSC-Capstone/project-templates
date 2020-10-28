
import pandas as pd

# Custom Features

def honorific(df):

    hnr = (
        df['Name']
        .str
        .extract(r' ([A-Z][a-z]+)\. ')
        .squeeze()
        .rename('Honorific')
    )

    return hnr


def last_name(df):

    lastname = (
        df['Name']
        .str
        .split(', ', n=1, expand=True)
        .loc[:, 0]
        .rename('Lastname')
        )

    return lastname


def sex2bin(df):
    
    return df['Sex'].replace({'male': 0, 'female': 1})


# putting features together


def feature_map():

    fmap = {
        "honorific": honorific,
        "last_name": last_name,
        "sex2bin": sex2bin
    }

    return fmap


def apply_features(df, feats, outfile=None):

    labels = df['Survived']

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

    

