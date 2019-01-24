# LearnFromBest
A platform for you to make most of the github by following the right person and reop regarding to your interest.

## Project Idea
Github is the most open source community in tech world. We share code, idea and publish new update with others.
Github is also one of the best sources for learning coding, but it do not have a system to help you find the right person and resources on specific area.
* Everyone want to learn from the best, I want to creat a data platform which can help you on this.

## Data Source
* Github archive : which stores all the eventbased github data every hour.
* 80~100G/month since 2012

## Tech Stack 
* Data Ingestion
Data stored in Bigquery, it will be cleaned with bigquery and clean data will be stored in Amazon S3

* Data Processing 
spark, algorithms(PageRank), will start from the most easy one.

* Database
Cassandra

* User Interface 
Flask

![Tech Stack](https://raw.githubusercontent.com/catherinesdataanalytics/LearnFromBest/master/pics/techFlow_Diagram.png)

## Engineering challenge
* Processing and cleaning 2.9TB github event data in json format, slice and find the right field 
* 80~100 G per month, and update every 1 hour in bigquery. Use airflow auto the whole processing.

## Alogorithms
Pagerank(Centrality Measures) and other network analysis algorithms.
![algorithms](https://raw.githubusercontent.com/catherinesdataanalytics/LearnFromBest/master/pics/algorithm.png)


## Business Value
If you want to learn "Golang" or other languages, this platform will recommend you the most valueble github user to follow and learn from based on network analysis results.
Show the show the 10 people to learn from or 10 best repo(based on some criteria like start and contribute fork).

## MVP
* data clean part - done with bigquery
* move data from Google storage to AWS S3
* S3 ->spark batch
* spark -> DB: TBD
* other analysis algo
