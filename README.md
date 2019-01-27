# LearnFromBest
A platform for you to make most of the github by following the right person regarding to your interest.

## Project Idea
Started from 2008, Github is now one of the most popular open source community in tech world. As of 2018, there are 28 million users and 57 million repositories, making it the largest host of source code in the world. 

Github is also one of the best sources for learning coding, we share code, publish new project, follow and learn from other users. But github do not have a system to help you find the right person and resources on specific area.

**Everyone wants to learn from the best, this project aims to creat a platform which can help you on finding the social influencer from the github network.**

## Data Source
* [Github archive](https://www.gharchive.org/) : GH Archive is a project to record the public GitHub timeline, which stores all the event based github.
* Data size: 80~100G/month since 2011
* Update frenquency: Update every 1 hour

## Tech Stack 

![Tech Stack](https://raw.githubusercontent.com/catherinesdataanalytics/LearnFromBest/master/pics/tech_flow_V2.png)

* **Data Ingestion**
   - Raw data stored in Bigquery, it will be cleaned with bigquery and will be transferred to AWS S3 bucket.
   - New coming data cleaning: use AWS lambda to clean the updated new coming data and append to historical data in HDFS.
   - HDFS: considering about the benefit for combining spark and HDFS, data will be stored to HDFS for data processing.

* **Data Processing** 
   - use spark for batch processing data on HDFS
   - algorithms(PageRank) written in scala 
   - other network analysis algorithms in graphX (TBD)

* **Database** 
   - Mysql, with 9 table corresponding to 9 languages. May be used for join later.

* **User Interface** 
   - Flask, user can select the language and they will get recommended users ranking by the social influencer score.

## Engineering challenge
* Data modeling: work on mapping user with languages from event data
* Processing and cleaning 2.9TB github event data in json format, slice and find the right field. - lambda 
* 80~100 G per month, and update every 1 hour in bigquery. Use airflow auto the whole processing. - airflow
* mysql connect and read from S3 using spark session 
* scala and graphX

## Alogorithms
Pagerank(Centrality Measures) and other network analysis algorithms.
* GraphX and more analysis soon.
<img src="https://raw.githubusercontent.com/catherinesdataanalytics/LearnFromBest/master/pics/SparkGraphx_Diagram.png " width="480">

## Business Value
If you want to learn "Golang" or other languages, this platform will recommend you the most valueble github user to follow and learn from based on network analysis results.
Show the 10 or N people to learn from based on network analysis result.

## MVP
* show sample result of the github user. User list which has a high pagerank score.
