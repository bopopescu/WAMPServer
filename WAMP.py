#Wyatt Humnphreys CNA 330 10/9/18
#Sources: https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python
#https://www.periscopedata.com/blog/python-create-table
#https://realpython.com/python-csv/

import os, csv, mysql.connector

con = mysql.connector.connect(user='root', password='',
                      host='127.0.0.1',
                      database='cna330')
cur = con.cursor()
cur.execute("CREATE TABLE t (Lab_name TEXT, Phone TEXT, Wheelchair TEXT, Hours TEXT, Tech_Support_Assisted TEXT, Organization TEXT, Location TEXT, Web_address TEXT);") # use your column names here

with open('Public_Computer_Access_Locations.csv','r') as fin: # Open the spreadsheet and give it the variable name "fin"
    #csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # reads a row from the csv and maps the info to an OrderedDict container. Also preserves order.
    to_db = [(i['Lab_name'], i['Phone'], i['Wheelchair'], i['Hours'], i['Tech_Support_Assisted'], i['Organization'], i['Location'], i['Web_address']) for i in dr] #Defines to_db as for each entry (i) in dr, make a list with entries in correct order.

cur.executemany("INSERT INTO t (Lab_name, Phone, Wheelchair, Hours, Tech_Support_Assisted, Organization, Location, Web_address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", to_db) # Plug in values from the to_db list into the columns of the 't' table based on their order from line 17. The '?' are used for number of items
con.commit()
con.close()