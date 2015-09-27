#!#/bin/bash
#Beginning of session on Sunday Sep. 27
echo $SHELL
set -o vi
wget https://s3.amazonaws.com/ucbdatasciencew205/labs/weblog_lab.csv
ls
history
pwd
ls
mkdir github
cd github
which git
git clone https://github.com/drewplant-MIDS/W205.git
ls
cd W205/
ls
LOAD DATA LOCAL INPATH '/mnt/weblog_lab.csv'
hive
