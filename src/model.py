
import pandas as pd
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

import joblib


def models():
    
    mdls = {
        "LogisticRegression": LogisticRegression,
        "RandomForestClassifier": RandomForestClassifier
    }

    return mdls


def model_build(
        features,
        tag,
        predictions_fp,
        mdl_fp,
        modeltype, 
        test_size, 
        **params):

    X_train, X_test, y_train, y_test = train_test_split(
        features, tag, test_size=test_size)

    mdl = models()[modeltype] # get model from dict
    mdl = mdl(**params) # instantiate model w/given params

    pl = Pipeline([
        ('one-hot', OneHotEncoder(handle_unknown='ignore')),
        ('mdl', mdl)
    ])

    pl.fit(X_train, y_train)
    predictions = pl.predict(X_test)
    out = pd.concat([pd.Series(predictions), y_test], axis=1)

    out.to_csv(predictions_fp)
    joblib.dump(pl, mdl_fp, compress=1)
    
    return out



