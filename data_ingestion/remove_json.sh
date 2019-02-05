#!/bin/bash

# This script download .json.gz file from github archive on hourly basis and move the unziped json file to HDFS

# Download gz file to masternode
## TODO: this will change with the time of day
# wget http://data.gharchive.org/2015-01-01-{0..23}.json.gz

# Unzip the file
gunzip -k *.gz

# Move the json file to HDFS
hadoop fs -mkdir /testdata
hadoop fs -put *.json /testdata

# End of this script
