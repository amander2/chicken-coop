import psycopg2 as pg
#import pandas as pd
import pandas.io.sql as psql

user_id = input('User ID : ')
print('NOTE: Both start and stop times MUST be in Unix Timestamp form. A conversion tool can be found \
at https://www.unixtimestamp.com/')
tstart = int(input('Enter event start time: '))
tstop = int(input('Enter event stop time: '))
bear_bull = input('Bull or Bear? ')

# establish connection with database
conn = pg.connect("dbname='chicken_coop' user='postgres' host='localhost' password='7337'")

# create cursor object
cur = conn.cursor()
cur.execute("insert into chicken_soup values (%s, %s, %s, %s)", (user_id, tstart, tstop, bear_bull))
# don't forget to commit your changes!!
conn.commit()

# reads sql table as dataframe
df = psql.read_sql("SELECT * FROM chicken_soup", conn)
print(df)
