import sqlite3

DATABASE = "solar_history.db"


def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        datetime TEXT,

        temperature REAL,

        humidity REAL,

        wind REAL,

        cloud REAL,

        dni REAL,

        power REAL

    )
    """)

    conn.commit()
    conn.close()


def save_prediction(result):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO predictions(

    datetime,

    temperature,

    humidity,

    wind,

    cloud,

    dni,

    power

    )

    VALUES(?,?,?,?,?,?,?)

    """,

    (

        result["datetime"],

        result["temperature"],

        result["humidity"],

        result["wind"],

        result["cloud"],

        result["dni"],

        result["power"]

    )

    )

    conn.commit()

    conn.close()


def get_history():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM predictions

    ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data