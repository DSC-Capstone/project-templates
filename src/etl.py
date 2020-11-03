import numpy as np
import pickle
import wget
import os
import tarfile

def get_data(data_cfg):
    url = 'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
    os.makedirs(data_cfg["outdir"])
    wget.download(url, data_cfg["outdir"])

    tar = tarfile.open(data_cfg["outdir"]+"/cifar-10-python.tar.gz", "r:gz")
    tar.extractall(path=data_cfg["outdir"])
    tar.close()
    return

def unpickle(file):
    with open(file, 'rb') as f:
        data = pickle.load(f, encoding="latin1")
    return data


def load_training_data(dataset_path):
    train_images = np.zeros([50000, 3072])
    train_labels = np.zeros([50000])

    start = 0
    n_images_in_a_file = 10000
    for i in range(1, 6):
        path = os.path.join(dataset_path,"cifar-10-batches-py/data_batch_{}".format(i))
        data_dict = unpickle(path)
        train_images[start: start + n_images_in_a_file, :] = data_dict["data"]
        train_labels[start: start + n_images_in_a_file] = data_dict["labels"]
        start += n_images_in_a_file

    return np.asarray(train_images, dtype=np.int), np.asarray(train_labels, dtype=np.int)


def load_test_data(dataset_path):

    path = os.path.join(dataset_path, "cifar-10-batches-py/test_batch")
    datadict = unpickle(path)
    test_images = datadict["data"]
    test_labels = datadict["labels"]
    return np.asarray(test_images, dtype=np.int), np.asarray(test_labels, dtype=np.int)