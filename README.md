# LearnFromBest
A platform for you to make most of the github by following the right person and reop.

## Project Idea
Github is the most open source community in tech world. We share code, idea and publish new update with others.
Github is also one of the best sources for learning coding, but it do not have a system to help you find the right person and resources on specific area.
I want to creat a data platform which can help you on this.


## Tech Stack 
* Data Ingestion
Data stored in Bigquery, it will be cleaned with bigquery and clean data will be stored in Amazon S3
![clean](https://github.com/Catherinesdataanalytics/LearnFromBest/pics/bigquery.png)

* Data Processing 
algorithms TBD, will start from the most easy one.

* Database
Cassandra

* User Interface 
Flask
![stack](https://github.com/Catherinesdataanalytics/LearnFromBest/pics/flow.png)


## Business Value
If you want to learn "Golang", this platform will tell you the most valueble people and repo to follow and learn from.
Show the 10 best repo(based on some criteria like update frequency) or show the 10 people to learn from.

## Data Source
* Github archive : which stores all the eventbased github data every hour.
* 80~100G/month since 2012

## 
