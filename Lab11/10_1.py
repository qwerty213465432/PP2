import psycopg2


conn = psycopg2.connect(
    host='localhost', 
    dbname='phnum', 
    user='postgres', 
    password='1221'
    )


cur = conn.cursor()

cur.execute('DROP TABLE ph_data;')

conn.commit()

cur.execute("""CREATE TABLE ph_data (
            name VARCHAR(255),
            adress VARCHAR(255) PRIMARY KEY,
            phone_number VARCHAR(20)
);
""")

conn.commit()

cur.execute("""INSERT INTO ph_data (name, adress, phone_number) VALUES 
            ('Ruslan', '24B202424', '+77007007070'),
            ('Mariya', '24B202425', '+77077077070');
""")

conn.commit()


cur.execute('SELECT name, adress, phone_number FROM ph_data')

print(cur.fetchall())
print(cur.fetchall())

cur.execute('SELECT name, adress, phone_number FROM ph_data')

print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())



cur.execute("""UPDATE ph_data
            SET phone_number = '+77718888870'
            WHERE adress = '24B202424';
""")

conn.commit()

cur.execute("""DELETE FROM ph_data
            WHERE adress = '24B202424';
""")

conn.commit()