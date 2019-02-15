#this is the script for extracting CommitCommentEvent from github arichive raw json file
#output will be saved into 'user,langueage' database for joining with user_follow,df_followed database

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import *
import datetime
import time
import re

hdfs_location = 'hdfs://ec2-52-33-137-78.us-west-2.compute.amazonaws.com:9000'
hdfs_readin_location = '{}/data_download/'.format(hdfs_location)
#location of files on hdfs for output of user language relationship
hdfs_language_location = '{}/language_data_cleaned/'.format(hdfs_location)

def classify_file(s):
    """
    function for classify files with their file endings
    input: (string)/somepath_to_file/app.py
    output: (String) Python
    """
    try:
        a = s.split('.')[-1]
        if a in ['java', 'class', 'jar']:
            return "Java"
        if a in ['go']:
            return 'Go'
        if a in ['js']:
            return 'JavaScript'
        if a in ['py', 'pyc', 'pyd', 'pyo', 'pyw' ,'pyz']:
            return 'Python'
        if a in ['rb']:
            return 'Ruby'
        if a in ['C', 'cc', 'cpp', 'cxx', 'c++','h','hpp', 'hxx', 'h++']:
            return 'Cplus'#'Cplus' means 'C++' here
        if a in ['php', 'phtml', 'php3', 'php4', 'php5', 'php7', 'phps', 'php-s']:
            return 'PHP'
        if a in ['cs']:
            return 'Csharp'#'Csharp'means C# here
    except:
        a = None
    return a

if __name__ == "__main__":
    try:
        #initial SparkSession
        spark = SparkSession.builder.appName("gitLanguage").getOrCreate()
    except:
        print('initial sparksession failed')

    try:
        #read json file from folder on hdfs with the latest unzipped json files.
        df = spark.read.json(hdfs_readin_location+'*.json')
    except:
        print('read data from hdfs failed, check hdfs location')
        print('current hdfs location is {}'.format(hdfs_readin_location))

    try:
        #slice out the events with CommitCommentEvent eventype
        df_comment = df[df.type.isin('CommitCommentEvent')]
    except:
        print('filter event with CommitCommentEvent failed, check accessibility for commit info from API ')

    try:
        #create column path with all path of the CommitCommentEvent and username extracted
        df_path = df_comment.withColumn('path',df_comment['payload']['comment']['path']).withColumn('username',df_comment['actor']['login'])
        ##TODO:change this with json extractor
    except:
        print('create new column failed')

    try:
        #use udf to construct the classify_file function for language matching
        matchLanguage = udf(classify_file, StringType())
    except:
        print('construct udf failed')

    try:
        #create column language with all the language classified and only select username and path columns
        df_language = df_path.withColumn('language',matchLanguage('path')).select('username','language')
    except:
        print('create language column failed')

    try:
        #drop file with none in language
        df_language_relationship = df_language.na.drop()
        #the output file name will be in format of '19-02-05-18-05.csv'
        outputfoldername = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
        #write to hdfs
        df_language_relationship.write.csv(hdfs_language_location + outputfilename)
    except:
        print('save to hdfs failed, check hdfs location {}'.format(hdfs_language_location + outputfilename))

    try:
        spark.stop()
    except:
        print('stop spark failed')
