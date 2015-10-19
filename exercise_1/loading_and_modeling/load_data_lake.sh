#!/bin/bash
#
#  Only mkdir in hdfs if the hospital_compare directory doesn't exist already...
if ! hdfs dfs -ls /user/w205/hospital_compare; then
	hdfs dfs -mkdir /user/w205/hospital_compare
fi

# Copy files from local nfs copy of *.csv to hdfs
cd /data/w205/hospitalData/strippedFiles/
for File in `ls`
	do
	echo $File
	hdfs dfs -put $File /user/w205/hospital_compare/
	done
