

def train(data, train_pct, outpath=None, **kwargs):

    X, y = ... # train-test split w/train_pct
    mdl = ... # use model params in kwargs

    mdl.train(X, y)
    
    if outpath is not None:
        mdl.save(outpath)

    return mdl


              
