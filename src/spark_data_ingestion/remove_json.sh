#!/bin/bash

# This script remove the spark processed downloaded jsonfile from HDFS

# Move the json file to HDFS
hadoop fs -rm  *.json /testdata

# End of this script
