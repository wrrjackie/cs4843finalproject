# 2022 NFL Best Prospects Based on RAS

This project was made to display the new 2022 NFL prospects and rank them based on their Relative Athletics Score that
is measured based on their physical attributes and combine stats.

## Google Cloud BigQuery

To work on this project, I was able to get a chance to work on one of Google's services: BigQuery

BigQuery is a powerful big data analytics platform that allowed me to set tables and compare prospects with each other
given by the dataset found on the RAS website: [RAS Football](ras.football)

## Basic Architecture
![image](https://user-images.githubusercontent.com/91208691/166843010-d275b244-68ae-444f-bf8d-20a4771d3ba1.png)

- BigQuery makes the Dataset Table
- Dataset Table is organized in SQL format for easy access
- Python Program extracts data from Dataset Table to get results
- Bash command line prints the result of the desired position

## Prerequisites

install python (I did so using the Windows Store)

The following packages need to be installed to access google cloud:
(make sure to have pip installed)

``` 
pip install --upgrade google-cloud 
```

``` 
pip install --upgrade google-cloud-bigquery 
```

``` 
pip install --upgrade google-cloud-storage 
```

## Things to Add
- Due to many complications I had with Flask, I wasn't able to create a webpage for users to interact from. 
- Make the searches more dynamic, like search by College
- Have the data more organized and sorted in the results
