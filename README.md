# LearnFromBest

A platform for you to make most of the github by discovering social influencers in github network regarding to your interest.

## Project Idea
Started from 2008, Github is now one of the most popular open source community in tech world. As of 2018, there are 28 million users and 57 million repositories, making it the largest host of source code in the world. 

Github is also one of the best sources for learning coding, we share code, publish new project, follow and learn from other users. But github do not have a system to help you find the right person and resources on specific area.

**Everyone wants to learn from the best, this project aims to creat a platform which can help you on finding the social influencer from the github network.**

## Data Source
* [Github archive](https://www.gharchive.org/) : GH Archive is a project to record the public GitHub timeline, which stores all the event based github. Weighing in over **3TB** total, this is the largest Bigquery dataset available on kaggle.
* Data size: 80~100G/month since 2011
* Update frenquency: Update every 1 hour

## Tech Stack 

![Tech Stack](https://raw.githubusercontent.com/catherinesdataanalytics/LearnFromBest/master/pics/tech_flow_V3.png)

* **Data Ingestion**
   - Raw data stored in Bigquery, it will be cleaned with bigquery and will be transferred to HDFS.
   - New coming data cleaning: use bigquery api and airflow scheduler to clean the updated new coming data and append to historical data in HDFS.
   - HDFS: All data will be stored to HDFS for data processing in spark.

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
* Centrality Measures: Pagerank 
* only people who used this language before has been included in the pagerank algorithms
* Community Detection: Strongly Connected Components
* GraphX and more analysis soon.
<img src="https://raw.githubusercontent.com/catherinesdataanalytics/LearnFromBest/master/pics/graphSpark.png " width="550">

## Business Value
1. If you want to learn "Golang" or other languages, this platform will recommend you the most valueble github user to follow and learn from based on network analysis results.
2. For example, Show the 10 or N people to learn from based on network analysis result.
Recommend community for colaboration.

## Temporal output
* show sample result of the github user. User list which has a high pagerank score.
* show the pagerank score which are defined by the user language.

- glassesfactory,68.0407463652.
- desandro,59.9803118883.
- defunkt,59.4355582686.
- mojombo,56.4538433468.
- visionmedia,51.6731830982.
- paulirish,50.9951976587.


## Further Questions
* The way to make the whole process real time or not need
* write test code 
* make data clean for deleted user and delete no following users
* move to scala, test structure in scala 
