# Getting the data for training
This folder has the code for getting all the data used for training the model.
## Dependencies
* scrapy
* beautifulsoup4
* requests
## Usage
The folders **gettitle, getlinks, convertlinks** are scrapy projects. The files **bs_digit.py, bs_iimnet.py, bs_paulnrogers.py** are used to fetch urls of e-Commerce sites using BeautifulSoup. The **data** folder contains the fetched URLs. The fetched URLs are used for training the model.

The list of e-Commerce websites were fetched from the following pages
```
* [http://www.thetoptens.com/ecommerce-websites-india/](http://www.thetoptens.com/ecommerce-websites-india/)
* [http://www.iimnet.com/profiles/blogs/list-of-e-commerce-companies-in-india](http://www.iimnet.com/profiles/blogs/list-of-e-commerce-companies-in-india)
* [http://www.digit.in/technology-guides/fasttrack-to-e-commerce/top-50-e-commerce-websites-in-india.html](http://www.digit.in/technology-guides/fasttrack-to-e-commerce/top-50-e-commerce-websites-in-india.html)
* [https://paulnrogers.com/top-50-ecommerce-websites/](https://paulnrogers.com/top-50-ecommerce-websites/)
```

*getlinks* project is used to get the e-Commerce site lists from [http://www.thetoptens.com/ecommerce-websites-india/](http://www.thetoptens.com/ecommerce-websites-india/). To run the project, open *getlinks* folder, then type the following command in the terminal
```
scrapy crawl links -o links.json
```
The output is saved in the project's top level directory with the name 'links.json'. It get us only the masked URLs.

*convertlinks* project is the continuation of the above project, and it is used to get the actual URL from the masked URL. To run the project, open *convertlinks* folder, then type the following command in the terminal
```
scrapy crawl convert -o convert.json
```
The output is saved in the project's top level directory with the name 'convert.json'.

The obtained files are of the JSON format, so to convert it to the required format (in this case to 'csv') run the `convert.py` file in the terminal
```
sudo python convert.py
```
The program saves the output in the *data* folder with the name 'converted.csv'.

*bs_digit.py* is used to get the e-Commerce site lists from [http://www.digit.in/technology-guides/fasttrack-to-e-commerce/top-50-e-commerce-websites-in-india.html](http://www.digit.in/technology-guides/fasttrack-to-e-commerce/top-50-e-commerce-websites-in-india.html). Run the file in the terminal as follows
```
sudo python bs_digit.py
```
The program saves the output in the *data* folder with the name 'digit.csv'.

*bs_iimnet.py* is used to get the e-Commerce site lists from [http://www.iimnet.com/profiles/blogs/list-of-e-commerce-companies-in-india](http://www.iimnet.com/profiles/blogs/list-of-e-commerce-companies-in-india). Run the file in the terminal as follows
```
sudo python bs_iimnet.py
```
The program saves the output in the *data* folder with the name 'iimnet.csv'.

*bs_paulnrogers.py* is used to get the e-Commerce site lists from [https://paulnrogers.com/top-50-ecommerce-websites/](https://paulnrogers.com/top-50-ecommerce-websites/). Run the file in the terminal as follows
```
sudo python bs_paulnrogers.py
```
The program saves the output in the *data* folder with the name 'paulnrogers.csv'.

After getting all the required data, the '.csv' files needs to be merged. Run the following command inside the *data* folder, in the teminal to merge the 'csvs'
```
sed 1d *.csv > merged.csv
```

Now we can use the 'merged.csv' which contains the URLs of e-Commerce sites, to get the title of each site.

The scrapy project 'gettitle' is used to get the titles for the URL's from 'merged.csv' file. To run the project, type the following command in the terminal from the 'gettitle' project's top level directory
```
scrapy crawl convert -o titles.json
```
The output is saved in the project's top level directory with the name 'titles.json'.

