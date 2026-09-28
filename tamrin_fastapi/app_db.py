import sqlite3

DBNAME = 'MoviesData.db'


def init_db():
    conn = sqlite3.connect(DBNAME)
    conn.close()
    create_table()


def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS movies
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    year TEXT,
    country TEXT,
    imdb_rate REAL
    )
    '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()


def insert_record(title, year, country, imdb_rate):
    query = '''
            INSERT INTO movies(title, year, country, imdb_rate)
            VALUES(?, ?, ?, ?)
            '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query, (title, year, country, imdb_rate))
    conn.commit()
    conn.close()


def select_all_records():
    query = '''SELECT * FROM movies'''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    rows = cursor.execute(query).fetchall()
    conn.close()
    return rows


def select_record_by_id(id):
    query = 'SELECT * FROM movies WHERE id = ?'
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    row = cursor.execute(query, (id,)).fetchone()
    conn.close()
    return row


def delete_record_by_id(id):
    query = '''DELETE FROM movies WHERE id = ?'''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()
    return f'id: {id} Deleted successfully'


def update_record_by_id(id, year, imdb_rate):
    query = '''
        UPDATE movies
        SET imdb_rate=? , year = ?
        WHERE id = ?
            '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query, (imdb_rate, year, id))
    conn.commit()
    conn.close()


# وقتی این فایل import شود، جدول ساخته می‌شود
init_db()