# Who Wins

Using Twitter API for opinion mining and sentiment analysis.

## Getting Started

#### Libraries

- pyspark : Apache Spark Library for Python (used for Machine Learning Algorithms)
  http://spark.apache.org/docs/2.2.0/api/python/index.html
- pandas : open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tool
  https://pandas.pydata.org/pandas-docs/stable/api.html
- numpy : efficient multi-dimensional container of generic data
  https://docs.scipy.org/doc/numpy-1.13.0/reference/
- polyglot : natural language pipeline
  https://github.com/aboSamoor/polyglot


#### How to install

With pip :
  > `pip3 install <library>`
  
With homebrew :
  >  `brew install <library>`

With Anaconda :
  > `conda install <library>`

##### Polyglot

Shell command line:
  > `sudo apt-get install python-numpy libicu-dev`

### Dataset

- Algorithm used for collecting the data :
  https://github.com/Jefferson-Henrique/GetOldTweets-python
  
- Download the dataset :
      -> directly from the website : https://www.kaggle.com/natmonkey/brexit-data-project-bdd/data
      -> with the shell command line :
        > `kaggle datasets download -d natmonkey/brexit-data-project-bdd`

- Data cleansing (csv file format):
  > `cat fichier | sort | uniq`
  
## Machine Learning

- Naive Bayes
- Logistic Regression
- Decision Tree
- Neural Network

## Authors

Mira Ait Saada, Alexandra Benamar, Cristel Dos Santos Catarino, Joel Oscar Dossa
