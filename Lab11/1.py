import csv
import psycopg2

# connecting to a database
conn = psycopg2.connect(
    host="localhost", 
    dbname="phnum", 
    user="postgres", 
    password="1221"
    )

# creating a cursor
# cursor is needed to interact with the database
cur = conn.cursor()

# csv file name
filename = 'phones.csv'

# reading csv
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, adress, phone_number = row
        # insertind data into the table
        cur.execute(f"""
                    INSERT INTO students_data 
                    VALUES ('{name}', '{adress}', {phone_number});
                    """)
    
    conn.commit()