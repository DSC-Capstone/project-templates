# Example Project: K-Means clustering on CIFAR-10

This project illustrates structuring a DS project clusters images of CIFAR-10 dataset. While the quality of the approach to building a model is not set to a high standard, the code is just non-trivial enough to illustrate how to handle making a DS project rerunnable and easy to navigate.

### Running the project
To install the dependencies, run the following command from the root directory of the project: 
pip install -r requirements.txt

### Building the project stages using run.py

* To get the data, from the project root dir, run python run.py data
  * This downloads the data from https://www.cs.toronto.edu/~kriz/cifar.html in the directory specified in config/data-params.json.
* To get the clustering results on the data, from the project root dir, run python run.py data model
  * This fetches the data and saves the output in data/out
