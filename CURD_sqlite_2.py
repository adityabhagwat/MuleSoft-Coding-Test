import sqlite3
#insert data
db_con = sqlite3.connect('MOVIES_DB')

db_con.execute('''Insert into MOVIES values('Lagaan','Aamir Khan','Gracy Singh',2001,'Ashutosh Gowarikar');''')

db_con.execute('''Insert into MOVIES values('3 idiots','Aamir Khan','Kareena Kapoor',2009,'Rajkumar Hirani');''')

db_con.execute('''Insert into MOVIES values('Avengers End-game','Robert Downey Jr','Scarlett Johnson',2019,'Joe Russo');''')

db_con.execute('''Insert into MOVIES values('Shershaah','Siddharth Malhotra','Kiara Advani',2021,'VishnuVardhan');''')

db_con.commit()

#Retrive Data
cur = db_con.cursor()
cur.execute('Select * from MOVIES')
rows = cur.fetchall()
for row in rows:
    print(row)

#retrive data using parameters
actor_name = 'Aamir Khan'
print("Retriving MOVIE Name using Actor Name",actor_name)
cur.execute('Select MOVIE_Name from MOVIES where Lead_actor = ?',(actor_name,))
rows2 = cur.fetchall()
for row2 in rows2:
    print(row2)