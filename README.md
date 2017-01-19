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