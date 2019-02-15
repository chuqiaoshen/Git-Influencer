#!/bin/bash

# This script is for running PageRank.py on 12 seperate languages on specific iterations

#iteration number
ITERATION=50

for LANGUAGE in 'C' 'Cplus' 'Csharp' 'Go' 'Java' 'JavaScript' 'Perl' 'PHP' 'Python' 'Ruby' 'Scala' 'Shell'
#python PageRank.py filename.csv numberforiteration(recommmend 50)
do
  #echo $LANGUAGE
  FULLPATH="path/to/followrelationship/file/$LANGUAGE.csv"
  #echo $FULLPATH
	spark-submit PageRank.py $FULLPATH $ITERATION
done

#END
