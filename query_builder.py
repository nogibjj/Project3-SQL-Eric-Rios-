import sqlite3

query1 = 'SELECT Name, Platform FROM games LIMIT 5'
query2 = 'SELECT Name, Platform, Year_of_Release FROM games WHERE Year_of_Release > 2000 LIMIT 10'
query3 = 'SELECT Name, Platform, Year_of_Release FROM games WHERE Year_of_Release > 2000 AND Platform = "PS2" LIMIT 20'


query4 = 'INSERT INTO games(Name, Platform, Year_of_Release,Genre, Publisher, Global_Sales) VALUES (?, ?, ?, ?, ?, ?)'

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


from csv import reader 
vg = []
with open('Video_Games_Sales_2016 - Copy.csv', encoding='utf-8') as file:
    csv_reader = reader(file)
    for row in csv_reader:
        vg.append(row)

for row in vg:
    cursor.execute(query4, row)

    
connection.commit()



for i in cursor.execute(query3):

    print(i)
