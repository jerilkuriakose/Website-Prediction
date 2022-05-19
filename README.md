# Website-Prediction
This project is predicting whether a given website is a e-Commerce website or not

## Overview
This is the code to predict whether a given website belongs to e-Commerce category or not.

## Dependencies
* scrapy
* sklearn
* pandas
* beautifulsoup4
* requests

### Installing dependencies
* pip install scrapy
* pip install sklearn
* pip install pandas
* pip install beautifulsoup4
* pip install requests

## Usage
This project consist of three folders
* GettingData
* PredictWebsite
* Results

*GettingData* folder constains the codes that are used in getting the data.
*PredictWebsite* folder constains the codes that are used for predicting the category of website.
*Results* folder contains the obtained results.

## Discussions
I have used only Multinomial Naive Bayes for predicting the category of the website. A hybrid algorithm could have been made by getting the results from multiple clssification technique.Decision tree would also give promising results, since the results require only True or False.

`CountVectorizer` is used to convert the text to vector format, we can get better results by using *word2vec.py* of **tensorflow** library.

## Revised Content

The **RevisedWork** directory contains the updated work. The revised results are saved as *revised_results.txt* inside the **results** folder

The following approaches can also be used to find out the website type:
* Find out the Content Management System (CMS) used, payment gateway from BuildWith and other sites.
* Analyse the following from different e-Commerce website:
    * Total number of words
    * Total number of links that redirects to a new page, that belongs to the root
    * Total number of images present
    * Checking for carousal / slider present
    * Checking for a search box

Once getting these information it can be used to find-out some intresting patterns.

https://anaconda-enterprise.s3.amazonaws.com/anaconda-enterprise-5.5.2-46-ge2465181d-g7.tar.gz
