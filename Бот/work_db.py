import sqlite3
import datetime
import pytz

DB_FILE = 'raketadb.db'


def create_tables():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            id_name INTEGER,
            user_name TEXT
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS user_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            message TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id_name)
        )
    ''')

    cur.execute('''
            CREATE TABLE IF NOT EXISTS car (
                id INTEGER PRIMARY KEY,
                num TEXT,
                name_car TEXT,
                work_description TEXT
            )
        ''')

    conn.commit()
    cur.close()
    conn.close()



def user_exists(user_id):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('SELECT id FROM users WHERE id_name = ?', (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result is not None



def insert_user(user_id, user_name):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('INSERT INTO users (id_name, user_name) VALUES (?, ?)', (user_id, user_name))
    conn.commit()
    cur.close()
    conn.close()



def insert_user_message(user_id, message):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    create_tables()
    current_datetime = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    cur.execute('INSERT INTO user_messages (user_id, message, timestamp) VALUES (?, ?, ?)',
                (user_id, message, current_datetime.strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    cur.close()
    conn.close()

def insert_car_info(num, name_car, work_description):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('INSERT INTO car (num, name_car, work_description) VALUES (?, ?, ?)', (num, name_car, work_description))
    conn.commit()
    cur.close()
    conn.close()