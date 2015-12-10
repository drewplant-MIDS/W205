
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

# Usage
Usage = 'Usage:  python finalresults.py word\n\
    where num = word = word being searched for in database...'

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

# Parse input arguments

if len(sys.argv) == 2:
    SearchWord = sys.argv[1]
elif len(sys.argv) == 1:
    SearchWord = ""
else:
    print "\n"
    print "   Error, invalid extra arguments %s" %(' '.join(sys.argv[2:]))
    print "   " + Usage
    print "\n"
    exit()
    

# Setup cursor object for doing postgresql querying
# # Create a new connect object
conn = psycopg2.connect(database="tcount", user="postgres", password="", host="localhost", port="5432")

# # Create a cursor
cur = conn.cursor()

# Either search for all words in table or only one word in table...
if SearchWord != "":
    cur.execute("SELECT word, count from Tweetwordcount WHERE word=%s;", (SearchWord,))
    ReturnRecords = cur.fetchall()
    # Check that word was found
    if len(ReturnRecords) > 0: 
        print "\n"
        print "Total number of occurrences of \"%s\": %d" %(ReturnRecords[0][0], ReturnRecords[0][1])
        print "\n"
    else:
        print "\n"
        print "Word \"%s\" not found in database yet." %(SearchWord)
        print "\n"

else: # If no word argument was given, return all records
    cur.execute("SELECT word, count from Tweetwordcount ORDER BY word asc")
    SearchRecs = cur.fetchall()
    OutString = ""
    for Tuple in SearchRecs[1:]:
        if len(OutString) > 0:
            OutString += ', '
        OutString += "(" + Tuple[0] + ", " + str(Tuple[1]) + ")"
    print OutString

# # Close the cursor
conn.close()
