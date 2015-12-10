# Submission for Exercise 2
#   Drew Plant
#   W205
#   Fall 2015
#   UC Berkeley - MIDS

To run this example, do the following:

1. Start the postgresql server
    /data/start_postgres.sh

2. Run postgresql as user postgres:
    psql -U postgres

2. Create a database called Tcount at the "postgres=#" prompt:
   postgres=#  create database Tcount;

3. Connect to the database Tcount at the "postgres=#" prompt:
   postgres=#  \c tcount;


3. Create a table called tweetwordcount at the tcount=# prompt:
   tcount=# CREATE TABLE tweetwordcount
   tcount=# (word TEXT PRIMARY KEY NOT NULL,
   tcount=# COUNT INT NOT NULL);

4. You can exit out of psql:
   tcount=# \q

5. Run the storm architecture from within directory $PWD/EX2Tweetwordcount
   cd EX2Tweetwordcount
   sparse run

6. In another terminal on the same machine, navigate to directory $PWD/scripts/
   
7. Run the scripts:
    A. python finalresults.py you
        Will print the number of occurrences of the word 'you'
    B. python finalresults.py 
        Will print out set of (word, number) tuples sorted alphabetically by word.

    C. python histogram.py 50 75
        Will print out the words with counts between 50 and 75 inclusive.

    
