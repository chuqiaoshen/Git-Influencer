#this is the script for extracting CommitCommentEvent from github arichive raw json file
#output will be saved into 'user,langueage' database for joining with user_follow,df_followed database

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("gitLanguage").getOrCreate()

df = spark.read.json('/home/jovyan/testGithubAPI/github_follow/*.json')

df_comment = df[df.type.isin('CommitCommentEvent')]

df_target = df_comment.withColumn('path',df_comment['payload']['comment']['path'])

all_path_python = df_target.select("path",df_target.path.startswith(".py"))
