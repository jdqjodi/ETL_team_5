# Are we going to Hawaii?

This  project is part II of the University of Toronto Data Analytics Boot Camp group projects series. 

#### -- Project Status: [Active]

## Project Intro/Objective

Our group will be exploring Honolulu, the hottest destination for Toronto people stranded in this weather. We are scraping the webs to find a good deal for hotels/air-bed-and-breakfasts as well as good restaurants to check out in April 2019. 

### Methods Used
* ETL
* Web scraping
* Data munging
* Database creation

### Technologies
* Python
* Beautiful Soup
* Pandas
* SQLAlchemy

## Project Description
1. We explored vacation-planning websites such as tripadvisor, cheapoair, expedia and airbnb to see if we can scrape their websites for data; in the end we were able to extract data from tripadvisor, vrbo (similar to airbnb) and yelp for hotels, resident rentals and restaurant ratings in Honolulu, Hawaii.
2. Using the python module requests we were able to establish a connection with website urls, and parse the html files into beautiful soup objects. Then we extracted titles of hotels and personal rentals, as well as price per night from tripadvisor and vrbo. We were also able to obtain restaurant titles and star ratings from yelp for hot restaurants in Honolulu.
3. After extracting the data, we used Pandas to format the data into three dataframes, for hotels, rentals and restaurants.
4. We exported the dataframes to CSV format and saved them [here](https://github.com/jdqjodi/ETL_team_5/tree/master/csvs).


## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.

    *If using offline data mention that and how they may obtain the data from the froup)*
    
3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)
4. etc...

## Contributing DSWG Members

**Team Leads (Contacts) : [Full Name](https://github.com/[github handle])(@slackHandle)**

#### Other Members:

|Name     |  Slack Handle   | 
|---------|-----------------|
|[Full Name](https://github.com/[github handle])| @johnDoe        |
|[Full Name](https://github.com/[github handle]) |  @janeDoe    |

## Contact
* If you haven't joined the SF Brigade Slack, [you can do that here](http://c4sf.me/slack).  
* Our slack channel is `#datasci-projectname`
* Feel free to contact team leads with any questions or if you are interested in contributing!
