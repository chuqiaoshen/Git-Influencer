#!/bin/bash

# This script is for extracting and moving the unziped json file to HDFS

cd /home/ubuntu/download_archive
# Unzip the archive data
gunzip -k *.gz

# Move the unzipped json file to HDFS
hadoop fs -mkdir /raw_data
hadoop fs -put *.json /raw_data

#remove files after unziped
rm -f *.gz
rm -f *.json
