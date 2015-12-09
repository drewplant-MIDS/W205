
"""
Python source code - search through postgresql table to find number of occurrences of particular word 
    Usage:
        python finalresults <word>
        =========================
            where:
                <word>  User-supplied word to locate in table.
                        If no argument <word> provided, then return
                        lines of tuples (<word>, <ntimes>) alphabetically sorted by
                        keyword.
"""
# Import code:
import psycopg2
import sys
import pprint

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

# Parse input arguments

# # Check if word argument is supplied
print "There are %d arguments given here. \nThe total command line was %s" %(len(sys.argv),str(sys.argv))
if len(sys.argv) == 2:
    SearchWord = sys.argv[1]
else:
    SearchWord = ""

# Setup cursor object for doing postgresql querying
# # Create a new connect object
conn = psycopg2.connect(database="test", user="postgres", password="", host="localhost", port="5432")

# # Create a cursor
cur = conn.cursor()

# Either search for all words in table or only one word in table...
if SearchWord != "":
    cur.execute("SELECT word, count from Tweetwordcount")

else:
    cur.execute("SELECT word, count from Tweetwordcount")
    SearchRecs = cur.fetchall()

# Collect occurrence of <word> in the postgresql database
# if tryWord in keys()

# # Close the cursor
conn.close()
