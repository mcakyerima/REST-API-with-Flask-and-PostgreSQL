import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

"""SQL QUERIES"""

# Ceate Rooms
CREATE_ROOMS_TABLE = (
    "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY AUTOINCREMENT, name TEST);"
)

# Create Temperature Table
CREATE_TEMPS_TABLE = """CREATE TABLE IF NOT EXISTS temperature (room_id INTEGER, temperature REAL,
                        date TIMESTAMP, FOREIGN KEY (room_id) REFERENCES rooms(id) ON DELETE CASCADE);"""

# Insert room
INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"

# Insert Temperature
INSERT_TEMP = (
    "INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);"
)

# Overall Number of Days
OVERALL_NUMBER_OF_DAYS = (
    """SELECT COUNT(DISTINCT DATE(date)) as days FROM temperatures;"""
)

# Avg temperature
GLOBAL_AVG = """SELECT AVG(temperature) as avg_temp FROM temperatures;"""


# Load our env variables
load_dotenv()


app = Flask(__name__)
url = os.getenv("DATABASE_URL")

# Connect to database
conn = psycopg2.connect(url)

@app.route("/")
def home():
    return "Helllo World!"

if __name__ == "__main__":
    app.run()
