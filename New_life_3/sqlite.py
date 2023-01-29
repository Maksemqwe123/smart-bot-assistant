import sqlite3 as sq


class Database:
    def __init__(self, db_file):
        self.connection = sq.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_table(self):
        with self.connection:
            return self.cursor.execute("""CREATE TABLE IF NOT EXISTS 'users_bot' (
            user_id INTEGER UNIQUE, 
            active INTEGER, 
            full_name TEXT,
            latitude INTEGER,
            longitude INTEGER
            )""")

    def create_profile(self, user_id: int):
        with self.connection:
            return self.cursor.execute("""SELECT user_id FROM users_bot WHERE user_id = ?""", (user_id, )).fetchall()

    # if not user:
    #     cur.execute("INSERT INTO profile VALUES(?);", (user_id))
    #     db.commit()

    def edit_profile(self, user_id, full_name):
        with self.connection:
            return self.cursor.execute("INSERT INTO 'users_bot' ('user_id', 'full_name') VALUES(?, ?)", (user_id, full_name, ))

    def all_user_db(self):
        with self.connection:
            return self.cursor.execute("SELECT * from 'users_bot'").fetchall()

    def local(self, user_id, latitude, longitude):
        with self.connection:
            return self.cursor.execute("""UPDATE 'users_bot' SET user_id = ? WHERE 'latitude' = ? AND 'longitude' = ?""", (user_id, latitude, longitude))
    #

    def check_city_user(self, latitude, longitude, user_id):
        with self.connection:
            return self.cursor.execute("SELECT 'latitude' = ? AND 'longitude' = ? FROM 'users_bot' WHERE user_id = ?",
                                       (latitude, longitude, user_id)).fetchall()

    def update_location(self, latitude, longitude, user_id):
        with self.connection:
            return self.cursor.execute("""UPDATE users_bot SET latitude = ?, longitude = ? WHERE user_id = ?""",
                                       (latitude, longitude, user_id))
    #
    # def city_user(self, city):
    #     with self.connection:
    #         return self.cursor.execute("INSERT INTO 'users' ('city') VALUES(?)", (city,))

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE users SET active = ? WHERE user_id = ?", (active, user_id, ))

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id, active FROM users_bot")
