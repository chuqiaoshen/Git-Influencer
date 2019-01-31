"""
Catherine Shen 20190124
PageRank implement by pyspark (sparksession version)
Input Format: csv with a,b in each line
Run:
python PageRank.py filename.csv numberforiteration
"""
#import library
from __future__ import print_function

import re
import sys
from operator import add

from pyspark.sql import SparkSession
from pyspark.sql.types import Row

#here you are going to create a function

#convert rdd to dataframe
#reference to https://stackoverflow.com/questions/39699107/spark-rdd-to-dataframe-python
def f(x):
    d = {}
    for i in x:
        d[x[0]] = x[1]
    return d

def computeContribs(followers, rank):
    """Calculates follower contributions to the rank of other followers.

       input
       followers:followers list
       rank:current rank of the user

       output
       yield rank to followers

    """
    num_followers = len(followers)
    for follower in followers:
        yield (follower, rank / num_followers)


def parseNeighborFollowers(followers):
    """Parses a followers pair string into followers pair.

       input "user1 user2"
       output user1,user2


    """
    parts = re.split(r'\,', followers)
    return parts[0], parts[1]


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: pagerank <file> <iterations>", file=sys.stderr)
        sys.exit(-1)

    print("Processing",file=sys.stderr)

    # Initialize the spark context.
    spark = SparkSession.builder.appName("PageRank").getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])

    #Initialization: Loads all followers from input file and initialize their neighbors.
    links = lines.map(lambda followers: parseNeighborFollowers(followers)).distinct().groupByKey().cache()

    # Loads all followers with other follower(s) link to from input file and initialize ranks of them to one.
    ranks = links.map(lambda follower_neighbors: (follower_neighbors[0], 1.0))

    #Iteration: Calculates and updates follower ranks continuously using PageRank algorithm.
    for iteration in range(int(sys.argv[2])):
        # Calculates follower contributions to the rank of other followers.
        contribs = links.join(ranks).flatMap(
            lambda follower_followers_rank: computeContribs(follower_followers_rank[1][0], follower_followers_rank[1][1]))

        # Re-calculates follower ranks based on neighbor contributions.
        ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85 + 0.15)

    # Collects all follower ranks and dump them to console.
    #for (link, rank) in ranks.collect():
        #print("%s %s." % (link, rank))
        #instead of the print, we store the output into mysql database with schema: username, score
    df = rdd.map(lambda x: Row(**f(x))).toDF()
    df.toPandas().to_csv("sample_file.csv", header=True)
    #get the df stored into db
    '''
    df.write.format('jdbc').options(
    url='jdbc:mysql://localhost/database_name',
    driver='com.mysql.jdbc.Driver',
    dbtable='DestinationTableName',
    user='your_user_name',
    password='your_password').mode('append').save()'''


    spark.stop()
