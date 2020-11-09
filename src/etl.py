

import os
import numpy as np
import pandas as pd


def generate_data(size=(1000, 3), **kwargs):

    n, k = size
    means = np.random.uniform(-3, 3, size=k)
    stds = np.random.uniform(size=k)
    
    data = np.random.normal(means, stds, size)
    data = pd.DataFrame(data, columns=['x_%d' % i for i in range(k)])    

    return data


def save_data(data, data_fp, **kwargs):

    os.makedirs(os.path.split(data_fp)[0], exist_ok=True)

    data.to_csv(data_fp, index=False)

    return 
