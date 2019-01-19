# Are we going to Hawaii?

This  project is part II of the University of Toronto Data Analytics Boot Camp group projects series. 

#### -- Project Status: [Near Completion]

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
3. After extracting the data, we used Pandas to clean and format the data into three dataframes, for hotels, rentals and restaurants.
4. We exported the dataframes to CSV format and saved them [here](https://github.com/jdqjodi/ETL_team_5/tree/master/csvs).
5. All data contained in the CSV files were uploaded to an in-memory relational database using SSQAlchemy.
6. The resulting tables: hotels, rentals and restaurants are final and able to be queried.


## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. CSV Data is being kept [here](https://github.com/jdqjodi/ETL_team_5/tree/master/csvs) within the *csvs* repo.
3. Data processing/transformation scripts are being kept in the *notebooks* [repo](https://github.com/jdqjodi/ETL_team_5/tree/master/notebooks).
4. Running the loading_to_db.ipynb file will create the in-memory database for querying.

#### All Members:

|Name     |  Slack Handle   | 
|---------|-----------------|
|[Paola Poblete](https://github.com/paola-poblete)| @Paola        |
|[Swati Madan](https://github.com/[github handle]) |  @Swati Madan    |
|[Bobby Bhattacharjee](https://github.com/write2bobby) |  @Bobby    |
|[Jodi Qiao](https://github.com/[github handle]) |  @Jodi    |
