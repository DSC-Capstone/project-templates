from sklearn.cluster import KMeans
import numpy as np
from scipy import stats

def classification_accuracy(prediction, ground_truth):
    ground_truth = ground_truth[:prediction.shape[0]]
    n_images = prediction.shape[0]
    x = prediction - ground_truth
    n_wrong_predictions = np.count_nonzero(x)
    accuracy = (n_images - n_wrong_predictions) / n_images

    return accuracy*100

def train(data, model_cfg):
    print("in train..")

    train_images, train_labels, test_images, test_labels = data

    print("in trsin.. loaded")
    n_classes = 10
    model = KMeans(n_clusters=model_cfg['n_clusters'], n_init=model_cfg['init'], max_iter=model_cfg['max_iter'])
    model.fit(train_images)

    print("in trsin.. fit done")
    # which images are assigned to each cluster:
    # 1. check all data points assigned to each cluster
    # 2. check actual labels of the data points assigned to each cluster
    # 3. assign the mode of actual labels to be the label for that cluster

    cluster_label_dict = {}
    for cluster_num in range(n_classes):
        idx = np.where(model.labels_ == cluster_num)[0]
        original_labels = np.take(train_labels, idx)
        mode = stats.mode(original_labels)[0][0]
        cluster_label_dict.update({cluster_num: mode})

    # prediction
    predicted_cluster = model.predict(test_images)
    predicted_labels = np.vectorize(cluster_label_dict.get)(predicted_cluster)

    accuracy = classification_accuracy(predicted_labels, test_labels)
    print(" K means clustering accuracy for cifar 10 = {}".format(accuracy))