from __future__ import absolute_import, print_function, unicode_literals
# psycopg2 for interacting with postgresql
import psycopg2

from collections import Counter
from streamparse.bolt import Bolt



class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

        # setup a connector object and connect to our postgresql database
        #Drew commenting out
        self.conn = psycopg2.connect(database="tcount", user="postgres", password="", host="localhost", port="5432")
        # Create a table
        ## Create a cursor
        self.cur = self.conn.cursor()
        #cur.execute('''CREATE TABLE tweetwordcount \
        #    (word TEXT PRIMARY KEY     NOT NULL, \
        #    COUNT INT      NOT NULL);''')
        #conn.commit()
        
    def process(self, tup):
        # Increment the local count
        newTweetWord = tup.values[0]
        # Update the word counter...
        self.counts[newTweetWord] += 1
        newTweetCount = self.counts[newTweetWord]
        # Check to see if word is in the table yet...
        self.cur.execute("SELECT word, count from Tweetwordcount WHERE word=%s;", (newTweetWord,))
        self.conn.commit()
        ReadLine = self.cur.fetchall()
        # Debug
        # print "Word %s is in the record." %(newTweetWord)

        # If word not yet in table...
        if len(ReadLine) == 0:
            # print "No records with word %s found...\n" %(newTweetWord)
            # Insert the word, count tuple
            self.cur.execute("INSERT INTO TWeetwordcount (word,count) \
            VALUES (%s, %s);", (newTweetWord, newTweetCount))
            # Commit update
            self.conn.commit()
 
        else:  # tweeted word is already so update by summing existing count and new count
            #NewCount = newTweetCount + ReadLine[0][1]
            self.cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s;", (newTweetCount, newTweetWord))
            # Commit update
            self.conn.commit()

        self.emit([newTweetWord, self.counts[newTweetWord]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (newTweetWord, self.counts[newTweetWord]))
        #self.log('%s: %d %g' %(newTweetWord, self.counts[newTweetWord], tup))
