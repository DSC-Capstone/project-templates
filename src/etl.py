import os
import pandas as pd


def get_data(indir, outdir):
    '''
    Reads the data by creating a symlink between the 
    location of the downloaded data and /data
    '''
    # first create the data directory
    directory = "data"
    parent_dir = "./"
    path = os.path.join(parent_dir, directory)

    os.mkdir(path)

    # create a convenient hierarchical structure of folders inside /data
    directory1 = "raw"
    directory2 = "temp"
    directory3 = "out"
    parent_dir = "./data/"
    
    os.mkdir(os.path.join(parent_dir, directory1))
    os.mkdir(os.path.join(parent_dir, directory2))
    os.mkdir(os.path.join(parent_dir, directory3))
    
    # create the symlink
    os.symlink(indir, outdir) 
        
    return pd.read_csv(outdir)
