#Sample code snippets for working with psycopg

#Connecting to a database
#Note: If the database does not exist, then this command will create the database

import psycopg2

conn = psycopg2.connect(database="test", user="postgres", password="", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor. 

cur = conn.cursor()
# cur.execute('''CREATE TABLE Tweetwordcount
#        (word TEXT PRIMARY KEY     NOT NULL,
#        count INT     NOT NULL);''')
# conn.commit()


#Running sample SQL statements
#Inserting/Selecting/Updating

#Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query, 
#and then read the query result a few rows at a time. One reason for doing this is
#to avoid memory overrun when the result contains a large number of rows. 

for KeyValueTups in [('dog',999), ('new', -7)]:
   # check to see if word is in table yet...
   # cur.execute("SELECT word, count from Tweetwordcount WHERE word=%s;", (KeyValueTups[0]))
   cur.execute("SELECT word, count from Tweetwordcount WHERE word=%s;", (KeyValueTups[0],))
   ReadRecords = cur.fetchall()
   print ReadRecords

   if len(ReadRecords) == 0:
      print "No records with word %s found...\n" %(KeyValueTups[0])
      print "Inserting new record here..."
      #Insert
      cur.execute("INSERT INTO Tweetwordcount (word,count) \
      VALUES (%s, %s);", (KeyValueTups[0], KeyValueTups[1]))
      conn.commit()

   else:  # Word is already there so update with new value of count...
      print ReadRecords
      print ReadRecords[0]
      NewCount = KeyValueTups[1]+ReadRecords[0][1]
      cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (NewCount, ReadRecords[0][0]))
      conn.commit()

#Select
cur.execute("SELECT word, count from Tweetwordcount")
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"
# Commit the commands
conn.commit()
conn.close()
