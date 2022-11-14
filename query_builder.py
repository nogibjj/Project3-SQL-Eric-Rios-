import sqlite3

table = 'CREATE TABLE games (id INTEGER PRIMARY KEY, Name TEXT, Platform TEXT, Year_of_Release INTEGER,Genre TEXT, Publisher TEXT, Global_Sales FLOAT)'
connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute(table)
connection.commit()