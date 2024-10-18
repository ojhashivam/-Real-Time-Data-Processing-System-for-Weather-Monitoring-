import sqlite3

def connect():
    conn = sqlite3.connect('weather_data.db')
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS daily_summary''')

    cursor.execute(
        ''' CREATE TABLE IF NOT EXISTS daily_summary(
        city TEXT,
        weather TEXT,
        date DATE,
        avg_temp REAL,
        max_temp REAL,
        min_temp REAL,
        dominant_condition REAL
        )'''
    )
    conn.commit()
    conn.close()

def store_daily_summary(city , weather , date, avg_temp, max_temp, min_temp, dominant_condition):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO daily_summary (city , weather , date, avg_temp, max_temp, min_temp, dominant_condition)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (city , weather , date, avg_temp, max_temp, min_temp, dominant_condition))
    conn.commit()
    conn.close()

def fetch_data():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute(
        '''SELECT 
            city AS city_name, 
            weather AS weather,
            date AS observation_date_and_time, 
            avg_temp AS average_temperature, 
            max_temp AS maximum_temperature, 
            min_temp AS minimum_temperature, 
            dominant_condition AS feels_like_temperature 
        FROM daily_summary'''
    )

    data = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    conn.close()
    
    result = [dict(zip(column_names, row)) for row in data]
    return result
