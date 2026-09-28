import sqlite3

DBNAME = 'MoviesDataa.db'

def init_db():
    conn = sqlite3.connect(DBNAME)
    conn.close()
    
###########################################################
# init_db()

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
#########################################################
# create_table()

def insert_record(title, year, country, imdb_rate):
    query = '''
            INSERT INTO movies(title, year, country, imdb_rate)
            VALUES(?, ?, ?, ?)
            '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query , (title, year, country, imdb_rate))
    conn.commit()
    conn.close()
########################################################
# insert_record('Inception', '2001', 'Germany', 7.9)
# insert_record('God Father', '2020', 'Denmark', 8.9)
# insert_record('seven', '2021', 'india', 8.4)
# insert_record('barby', '2012', 'america', 6.7)
# insert_record('the lord of the rings', '1997', 'england', 8.1)


def select_all_records():

    # query = '''SELECT title, year FROM movies'''
    query = '''SELECT * FROM movies'''

    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    rows = cursor.execute(query).fetchall()
    conn.close()
    return rows
########################################################
# print(select_all_records()

def select_record_by_title(title):
    query = 'SELECT * FROM movies WHERE title = ?'
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    row = cursor.execute(query, (title,)).fetchone()
    conn.close()
    return row
#############################################################
# print(select_record_by_title(god father))

def select_record_by_imdb_rate(imdb_rate):
    query = 'SELECT * FROM movies WHERE imdb_rate = ?'
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    row = cursor.execute(query, (imdb_rate,)).fetchone()
    conn.close()
    return row
#############################################################
# print(select_record_by_imdb_rate(8.9))



def delete_record_by_title(title):
    query = '''DELETE FROM movies WHERE title = ?'''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query, (title,))
    conn.commit()
    conn.close()
    return f'title: {title} Deleted successully'
#################################################################
# ids = [1, 4, 6]
# for item in ids:
#     delete_record_by_title(item)
# print(delete_record_by_title(god father))

def update_record_by_title(title, year,country, imdb_rate):
    query = '''
        UPDATE movies
        SET imdb_rate=? , year = ? , country = ?
        WHERE title = ?
            '''
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute(query, (imdb_rate, year, country, title))
    conn.commit()
    conn.close()

##################################################################
# update_record_by_id(seven, '2021', iran , 4.6)