#!/bin/bash

# This script is for download .json.gz file from github archive on hourly basis and move the unziped json file to HDFS

#download archive data using python
python /home/ubuntu/data_injestion/download_archive.py

cd /home/ubuntu/download_archive
# Unzip the archive data
gunzip -k *.gz

# Move the unzipped json file to HDFS
hadoop fs -mkdir /raw_data
hadoop fs -put *.json /raw_data

#remove files after unziped
rm -f *.gz
rm -f *.json

#get the follow relationship from download github archive data
spark-submit get_follow_relationship.py

#get the language relationship from download github archive data
spark-submit get_language_relationship.py

#delete the raw data (only use for history data cleaning part)
#hadoop fs -rm  *.json /raw_data

# End
