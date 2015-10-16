#!/bin/bash
# mkdir
#  Only do this if it hasn't already been done...
# hdfs dfs -mkdir /user/w205/hospital_compare
hdfs dfs -put /data/w205/hospitalData/strippedFiles/*.csv /user/w205/hospital_compare/
