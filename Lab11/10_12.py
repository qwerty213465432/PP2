import psycopg2


conn = psycopg2.connect(
    host='localhost', 
    dbname='phnum', 
    user='postgres', 
    password='1221'
    )


cur = conn.cursor()


#cur.execute('DROP TABLE ph_data;')

conn.commit()


cur.execute("""CREATE TABLE ph_data (
            name VARCHAR(255),
            adress VARCHAR(255) PRIMARY KEY,
            phone_number VARCHAR(20)
);
""")

conn.commit()

import csv

filename = 'phones.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, adress, phone_number = row
        
        #№1
        cur.execute(f"""INSERT INTO ph_data (name, adress, phone_number) VALUES 
                    ('{name}', '{adress}','{phone_number}');
        """)

        #№2

        
        name = input("Enter user name: ")
        phone_number = input("Enter phone number: ")

        
        cur.execute("INSERT INTO ph_data (user_name, phone_number) VALUES (%s, %s)", (name, phone_number))



        #№3
        cur.execute("""UPDATE ph_data
            SET phone_number = '+77718888870'
            WHERE adress = '24B202424';
        """)

        conn.commit()



        #№4
     
        cur.execute("SELECT * FROM ph_data")

      
        cur.execute("SELECT * FROM ph_data WHERE user_name = %s", (name,))

        
        cur.execute("SELECT * FROM ph_data WHERE phone_number = %s", (phone_number,))





        #№5
        
        cur.execute("DELETE FROM ph_data WHERE user_name = %s", (name,))

       
        cur.execute("DELETE FROM ph_data WHERE phone_number = %s", (phone_number,))


        conn.commit()