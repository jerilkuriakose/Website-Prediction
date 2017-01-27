# Revised work

Two methods have been used to find out the type of website. The first method did not give any satisfactory results. The second method was giving some promising results.

### Method 1

It uses [http://whatcms.org/](http://whatcms.org/) to finf out the type of CMS used by the website. The method returns a list with the CMS used, but most of the values were nan. No promising results were obtained.

#### Dependencies

* BeautifulSoup4
* Requests

### Method 2

This method uses [https://builtwith.com/](BuildWith) site to get the infromation about the type of website. If it is an e-Commerce website it informs about the platform used for making it.

The results from method 2 is saved as *results_revised.txt* inside the **results** folder

The following approaches can be used to find out the website type:
* Find out the Content Management System (CMS) used, payment gateway from BuildWith and other sites.
* Analyse the following from different e-Commerce website:
    * Total number of words
    * Total number of links that redirects to a new page, that belongs to the root
    * Total number of images present
    * Checking for carousal / slider present
    * Checking for a search box

Once getting these information it can be used to find-out some intresting patterns.