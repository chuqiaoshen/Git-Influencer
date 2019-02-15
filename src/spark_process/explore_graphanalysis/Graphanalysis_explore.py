#this python file is an exploratory analysis using graphframes

from pyspark import *
from pyspark.sql import *
from graphframes import *
from pyspark.sql.functions import udf

spark = SparkSession.builder.appName('explore').getOrCreate()

vertices = spark.createDataFrame([('1', 'Carter', 'Derrick', 50),
                                  ('2', 'May', 'Derrick', 26),
                                 ('3', 'Mills', 'Jeff', 80),
                                  ('4', 'Hood', 'Robert', 65),
                                  ('5', 'Banks', 'Mike', 93),
                                 ('98', 'Berg', 'Tim', 28),
                                 ('99', 'Page', 'Allan', 16)],
                                 ['id', 'name', 'firstname', 'age'])
edges = spark.createDataFrame([('1', '2', 'friend'),
                               ('2', '1', 'friend'),
                              ('3', '1', 'friend'),
                              ('1', '3', 'friend'),
                               ('2', '3', 'follows'),
                               ('3', '4', 'friend'),
                               ('4', '3', 'friend'),
                               ('5', '3', 'friend'),
                               ('3', '5', 'friend'),
                               ('4', '5', 'follows'),
                              ('98', '99', 'friend'),
                              ('99', '98', 'friend')],
                              ['src', 'dst', 'type'])

g = GraphFrame(vertices, edges)
## Take a look at the DataFrames
g.vertices.show()
g.edges.show()
## Check the number of edges of each vertex
g.degrees.show()

copy = edges

@udf("string")
def to_undir(src, dst):
    if src >= dst:
        return 'Delete'
    else :
        return 'Keep'
copy.withColumn('undir', to_undir(copy.src, copy.dst))\
.filter('undir == "Keep"').drop('undir').show()
## for efficiency, it's better to avoid udf functions where possible ## and use built-in pyspark.sql.functions instead.


g.vertices.filter("age > 30").show()
g.inDegrees.filter("inDegree >= 2").sort("inDegree", ascending=False).show()
g.edges.filter('type == "friend"')


sc.setCheckpointDir('graphframes_cps')
g.connectedComponents().show()

#triangle counts
g.triangleCount().show()
pr = g.pageRank(resetProbability=0.15, tol=0.01)

## look at the pagerank score for every vertex
pr.vertices.show()
## look at the weight of every edge
pr.edges.show()
