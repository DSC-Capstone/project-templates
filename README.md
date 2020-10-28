# Example Project: Titanic Prediction 

This project illustrates structuring a DS project that approaches the
very simple task of predicting who survives on the titanic. While the
quality of the approach to building a model is not set to a high
standard, the code is just non-trivial enough to illustrate how to
handle making a DS project rerunnable and easy to navigate.

## Running the project

* To get the data from Kaggle, create an account and request an API
  Token ("My Account" => "Create New API Token").
* Save this token (or create a shortcut) as `.env/kaggle.json` in the
  project root directory.
* To install the dependencies, run the following command from the root
  directory of the project: `pip install -r requirements.txt`
  
### Building the project stages using `run.py`

* To get the data, from the project root dir, run `python run.py data`
  - This downloads the data from Kaggle in the directory specified in
    `config/data-params.json`.
* To get the data, from the project root dir, run `python run.py data
  features`
  - This downloads the data, then creates features (defined in
    `src/features.py`) and saves them in the location specified in
    `features-params.json`.
* To get the data, from the project root dir, run `python run.py data
  features model`
  - This downloads the data, creates the features, then trains a model
    (with parameters specified in `config`). It writes both the
    prediction from the model for analysis and pickles the model using
    `joblib`.


### A few notes on the anatomy of the project:
* It downloads the titanic dataset from kaggle, using an API token.
* It allows the user to create a 'bank' of features for a classifier
  to use and specify which to include in configuration files.
* The configuration files are the result of experimentation in
  developing the model. You may have multiple config files for
  different choices of features/models -- this is a way to
  parameterize experiments.
* The way `run.py` is setup, when running the project, you must run it
  from the beginning (always starting with pulling the data). This is
  bad form. How can you fix `run.py` so that if you already have the
  data downloaded, you can run e.g. `python run.py features` successfully.
* Notebook examples will be created later. You can import the library
  code from `src` to use in notebooks (just like `run.py`).
  

**Try running this yourself! (It will involve getting a Kaggle account
and downloading the API Token).**


