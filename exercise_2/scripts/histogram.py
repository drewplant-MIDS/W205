"""
Python source code - search through postgresql table to find number of occurrences of particular word 
    Usage:
        python histogram k1 k2
        =========================
            where:
                k1, k2  Bin limits for number of occurrences for words
                            where k1 > k2                       
                Output:  all words occurring between k1 and k2 times in the database.
"""
# Import code:
import psycopg2
import sys
import pprint
import argparse # For easy argument parsing

# Usage
parser = argparse.ArgumentParser(description='Locate words with wordcount in given bin range')
parser.add_argument("k1", type=int, help='k1 is min bin count for word' )
parser.add_argument("k2", type=int, help='k2 is max bin count for word and k1 <= k2' )
# Produce an args object
args = parser.parse_args()


Usage = 'Usage:  python histogram.py k1 k2\n\
    where k1, k2 = bin values for word counts in database\n\
          and 0 < k1 <= k2'

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

# Error checking:
if not (args.k1 <= args.k2):
    print "\n"
    print "Error:  k1 must be < or = to k2!"
    print Usage
    print "\n"
    exit()
elif not (args.k1 > 0):
    print "\n"
    print "Error:  k1 and k2 must be greater than 0!"
    print Usage
    print "\n"
    exit()


# Setup cursor object for doing postgresql querying
# # Create a new connect object
conn = psycopg2.connect(database="tcount", user="postgres", password="", host="localhost", port="5432")

# # Create a cursor
cur = conn.cursor()

# Either search for all words in table or only one word in table...
if args.k1 == args.k2:
    cur.execute("SELECT word, count from Tweetwordcount WHERE count=%s ORDER BY count desc;", (args.k1,))
else:
    cur.execute("SELECT word, count from Tweetwordcount WHERE (count>=%s) AND (count<=%s) ORDER BY count desc;", (args.k1,args.k2)) 
ReturnRecords = cur.fetchall()
if len(ReturnRecords) > 0:
    print "\n"
    OutString = ""
    for Tuple in ReturnRecords:
        OutString += "     " + Tuple[0] + ": " + str(Tuple[1]) + "\n"
    print OutString
    print "\n"
else:
    print "\n"
    print "No words found in database with counts of k1 = %d and k2 = %d" %(args.k1,args.k2)
    print "\n"


# # Close the cursor
conn.close()
