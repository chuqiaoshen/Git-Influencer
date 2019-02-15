# Git-Influencer

A platform for you to make most of the github by discovering social influencers in github network regarding to your interest.

## Project Idea
Started from 2008, Github is now one of the most popular open source community in tech world. As of 2018, there are 28 million users and 57 million repositories, making it the largest host of source code in the world.

Github is also one of the best sources for learning coding, we share code, publish new project, follow and learn from other users. But github do not have a system to help you find the right person and resources on specific area.

**Everyone wants to learn from the best, this project aims to creat a platform which can help you on finding the social influencers from the github network.**

## Data Source
* [Github archive](https://www.gharchive.org/) : GH Archive is a project to record the public GitHub timeline, which stores all the event based github. Weighing in over **3TB** total, this is the largest Bigquery dataset available on kaggle.
* Data size: 80~100G/month since 2011
* Update frenquency: Update every 1 hour

## Tech Stack

![Tech Stack](https://raw.githubusercontent.com/catherinesdataanalytics/LearnFromBest/master/pics/tech_flow_V4.png)

* **Data Ingestion**
   - Historical data: Raw data stored in github Archive, it is scheduled to be downloaded with python and Airflow and saved to HDFS. 
   - New coming data: use github Archive api and airflow scheduler to clean the updated new coming data and append to historical data in HDFS.
   - HDFS: All data in HDFS will be cleaned with spark and saved for data processing in spark.

* **Data Processing**
   - use spark for batch processing data on HDFS
   - PageRank and other network analysis algorithms in graphX

* **Database**
   - Mysql, with 10 table corresponding to 10 languages.

* **User Interface**
   - Dash, user can select the language and they will get recommended users ranking by the social influencer score.

## Engineering challenge
* Data modeling: find clues from raw json event data for mapping users with languages.
* Data size and update: Processing and cleaning 2.9TB github event data, combining both historical data cleaning and new coming data cleaning: 80~100 G per month, and update every hour. Use airflow auto the whole processing. 

## Alogorithms
* Centrality Measures: Pagerank
* only people who used this language before has been included in the pagerank algorithms
* Community Detection: Strongly Connected Components
* GraphX and more analysis in the future.

## Business Value
1. If you want to learn "Golang" or other languages, this platform will recommend you the most valueble github user to follow and learn from based on network analysis results.
2. For example, Show N people to learn from based on network analysis result.
Recommend community for colaboration.


## Further Improvement
* Explore HDFS data storage efficiency - Parquet
* Try different classification metric for discovering more user topics
* Use more Graph analysis algorithms in GraphX

## Dashboard and PPT
[Git Influencer dashboard](http://bit.ly/Git-Influencer)
[Project Slides](https://www.slideshare.net/CatherineShen10/git-influencer-catherine-shen)
[Demo video](https://youtu.be/bOVR8one7pY)
