import sqlite3

query1 = 'SELECT Name, Platform FROM games LIMIT 5'
query2 = 'SELECT Name, Platform, Year_of_Release FROM games WHERE Year_of_Release > 2000 LIMIT 10'
query3 = 'SELECT Name, Platform, Year_of_Release FROM games WHERE Year_of_Release > 2000 AND Platform = "PS2" LIMIT 20'


query4 = 'INSERT INTO games(Name, Platform, Year_of_Release,Genre, Publisher, Global_Sales) VALUES (?, ?, ?, ?, ?, ?)'

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


from csv import reader 
vg = []
with open('Video_Games_Sales_2016 - Copy.csv') as file:
    csv_reader = reader(file)
    for row in csv_reader:
        vg.append(row)

for row in vg:
    cursor.execute(query4, row)
    # the first elements in the row
    # Assert : First Row : ['Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher', 'Global_Sales'], has to be its own file, 
    # asserts for all queries
    # Test_File, is run by Github Actions, in make test
    
connection.commit()



for i in cursor.execute(query3):

    print(i)

# Missing : Github actions 
# test file 
# external connections to database--Recc : Postgres-Alfredo's/Rec:BigQuery-Google/AWS-RDS/
# Alfredo - Demo Github - Postgres
# Secrets, passwords, connections to database (PG/BQ)


#Project 4
# API to connect to database
# Microservice : Do something specific, and do it well - quey the database
# Streamlit/Fast API - Frontend, a web app where users can input what they want - Noah - Continuous Deployment
# Apprunner - AWS - Deploy a web app - Noah, on linkedin, repos