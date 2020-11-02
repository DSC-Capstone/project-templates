# Example Project: Statistical Data Analysis

__This project template demonstrates/highlights__: hypothesis testing, exploratory data analysis through a jupyter notebook, data cleaning and determining the statistical significance using a t-test.

This project is a template for structuring the data science project for DSC180. This project explores the question: Are first-born babies more likely to arrive late or early?
We start by assuming the null hypotheis which is first borns are likely to arrive at the same time as all newborn babies. And we design a t-test to determine if there is a significant difference between the means of the first-born babies and all newborn babies.


## Retrieving the data locally:

(1) Download the data file 2002FemPreg.dat.gz, from the Think stats website http://www.greenteapress.com/thinkstats/nsfg.html.

(2) Edit the file: __config/data-params.json__ to include the path/location of the downloaded data in the value of the _indir_ key


## Running the project

* To install the dependencies, run the following command from the root directory of the project: `pip install -r requirements.txt`

  
### Building the project stages using `run.py`

* To get the data, from the project root dir, run `python run.py data features`
  - This fetches the data, creates features, cleans data and saves the data in data/temp directory.
* To get the results of statistical test, from the project root dir, run `python run.py data features model`
  - This fetches the data, creates the features, creates a statistical model and saves the result of the ttest in the data/out directory.
  
## Reference
Think Stats: Exploratory Data Analysis in Python by Allen B. Downey
