#this is the pyspark file for cleaning data from github archive json files and cleaned into 'user_follow,user_followed' format
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("GetFollow").getOrCreate()

#readin data from json format
df = spark.read.json('/Directory_to_jsonfiles/*.json')

#slice out the event type in FollowEvent
#create new column user_follow and user_followed
df_follow_event = df[df.type.isin('FollowEvent')].withColumn('user_follow',df_follow['actor']['login']).withColumn('user_followed',df_follow['payload']['target']['login'])

df_follow_relationship = df_follow_event.select('user_follow','user_followed')

#TODO
#save result to hdfs for further spark processing
