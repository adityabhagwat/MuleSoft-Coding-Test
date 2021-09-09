import sqlite3

#create db

db_con = sqlite3.connect('MOVIES_DB')

#create table
db_con.execute('CREATE TABLE MOVIES (MOVIE_Name Text,Lead_Actor Text,Lead_Actress Text,Release_Year INTEGER,DIRECTOR_Name Text);')

