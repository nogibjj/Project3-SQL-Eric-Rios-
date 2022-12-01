import sqlite3

drop_table = 'DROP TABLE IF EXISTS games'
table = 'CREATE TABLE games (id INTEGER PRIMARY KEY, Name TEXT, Platform TEXT, Year_of_Release INTEGER,Genre TEXT, Publisher TEXT, Global_Sales FLOAT)'
connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute(drop_table)
cursor.execute(table)


connection.commit()

