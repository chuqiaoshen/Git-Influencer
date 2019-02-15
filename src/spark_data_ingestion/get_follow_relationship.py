#this is the pyspark file for cleaning data from github archive json files and cleaned into 'user_follow,user_followed' format
import time
import datetime
from pyspark.sql import SparkSession


hdfs_location = 'hdfs://ec2-52-33-137-78.us-west-2.compute.amazonaws.com:9000'
#location of files on hdfs for raw json readin
hdfs_readin_location = '{}/data_download/'.format(hdfs_location)
#location of files on hdfs for output of user follow relationship
hdfs_follow_location = '{}/follow_data_cleaned/'.format(hdfs_location)

if __name__ == "__main__":

    try:
        spark = SparkSession.builder.appName("GetFollow").getOrCreate()
    except:
        print('SparkSession start failed')

    try:
        #read json file from data_download folder on hdfs with the latest unzipped json files.
        df = spark.read.json("{}*.json".format(hdfs_readin_location))
    except:

        print('Spark readin json failed, check hdfs_readin_location')
        print('current readin location is {}'.format(hdfs_readin_location))

        #slice out the event type with FollowEvent          #create new column user_follow and user_followed
    try:
        df_follow_event = df[df.type.isin('FollowEvent')]
    except:
        print('failed to slice out FollowEvent')

    try:
        df_follow = df_follow_event.withColumn('user_follow',df_follow_event['actor']['login']).withColumn('user_followed',df_follow_event['payload']['target']['login'])
    except:
        print('')

    try:
        #select the user_follow and user_followed columns for saving
        df_follow_relationship = df_follow.select('user_follow','user_followed')
    except:
        print('failed to select user follow relationship')

    try:
        #the output file name will be in folder of '19-02-05-18-05'
        outputfilename = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")

        #save result to hdfs in csv format for further spark processing
        df_follow_relationship.write.csv(hdfs_follow_location + outputfilename)
    except:
        print('data save to hdfs failed, check output directory name')
        print('current save location is {}'.format(hdfs_follow_location + outputfilename))

    try:
        spark.stop()
    except :
        print("failed to stop spark")
