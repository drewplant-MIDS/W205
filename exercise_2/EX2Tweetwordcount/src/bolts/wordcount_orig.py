from __future__ import absolute_import, print_function, unicode_literals
# psycopg2 for interacting with postgresql
import psycopg2

from collections import Counter
from streamparse.bolt import Bolt



class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

        # setup a connector object and connect to our postgresql database
        # conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        # Create a table
        ## Create a cursor
        # cur = conn.cursor()
        # cur.execute('''CREATE TABLE tweetwordcount \
        #    (word TEXT PRIMARY KEY     NOT NULL, \
        #    COUNT INT      NOT NULL);''')
        # conn.commit()
        # conn.close()
        
    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
