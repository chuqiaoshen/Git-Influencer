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

# End of this script
