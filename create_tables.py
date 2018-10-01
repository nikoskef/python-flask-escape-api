import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS rooms(" \
                   "id INTEGER PRIMARY KEY," \
                   " company text," \
                   " location text," \
                   " name text," \
                    "description text," \
                    "rateofescape text," \
                    "img text," \
                    "duration text," \
                    "playedon text " \
                    ")"
cursor.execute(create_table)

cursor.execute("INSERT INTO rooms VALUES ("
               "NULL, "
               "'Nikos Escape The Room', "
               "'Ayia Napa', "
               "'The Nun',"
               "'In a forgotten, dark basement, evil spirits call you. Your fear and your curiosity, their greatest strength! Will you respond to their call ..? The largest and first horror Escape room in Cyprus! The atmospheric sounds and terrifying scenery, combined with the Live acting of the room, will make you scream!',"
               "'9/10',"
               "'nun.jpg',"
               "'90 minutes',"
               "'18-03-2018 , 17:00')")

cursor.execute("INSERT INTO rooms VALUES ("
               "NULL, "
               "'Nikos Escape The Room', "
               "'Ayia Napa', "
               "'Conjuring',"
               "'In a forgotten, dark basement, evil spirits call you. Your fear and your curiosity, their greatest strength! Will you respond to their call ..? The largest and first horror Escape room in Cyprus! The atmospheric sounds and terrifying scenery, combined with the Live acting of the room, will make you scream!',"
               "'10/10',"
               "'conjuring.jpg',"
               "'180 minutes',"
               "'28-03-2017 , 17:00')")

connection.commit()

connection.close()