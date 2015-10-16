#!/bin/bash
# mkdir
#  Only do this if it hasn't already been done...
# hdfs dfs -mkdir /user/w205/hospital_compare
cd /data/w205/hospitalData/strippedFiles/
for File in `ls`
	do
	echo $File
	hdfs dfs -put $File /user/w205/hospital_compare/
	done
