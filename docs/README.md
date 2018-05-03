# Who Wins

Using Twitter API for opinion mining and sentiment analysis.

## Implementation

Language version : Python 3.6 <br />
Operating System : Ubuntu 16.04, Windows 10 and MacOS High Sierra.

## Getting Started

### Libraries

- pyspark : Apache Spark Library for Python (used for Machine Learning Algorithms)
  http://spark.apache.org/docs/2.2.0/api/python/index.html
- pandas : open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tool
  https://pandas.pydata.org/pandas-docs/stable/api.html
- numpy : efficient multi-dimensional container of generic data
  https://docs.scipy.org/doc/numpy-1.13.0/reference/
- polyglot : natural language pipeline
  https://github.com/aboSamoor/polyglot


#### How to install

With pip : <br />
  > `pip3 install <library>`
  
With homebrew : <br />
  > `brew install <library>`

With Anaconda : <br />
  > `conda install <library>`

##### Installing polyglot ...

Shell command line: <br />
  > `sudo apt-get install python-numpy libicu-dev`

## Dataset

- Algorithm used for collecting the data : <br />
  https://github.com/Jefferson-Henrique/GetOldTweets-python
  
- Download the dataset : <br />
      - directly from the website : <br />
           https://www.kaggle.com/natmonkey/brexit-data-project-bdd/data <br />
      - with the shell command line : <br />
        `kaggle datasets download -d natmonkey/brexit-data-project-bdd` <br />

- Data cleansing (csv file format): <br />
  > `cat fichier | sort | uniq`
  
## Machine Learning

- Naive Bayes
- Logistic Regression
- Decision Tree
- Neural Network

## Authors

Mira Ait Saada, Alexandra Benamar, Cristel Dos Santos Catarino, Joel Oscar Dossa
