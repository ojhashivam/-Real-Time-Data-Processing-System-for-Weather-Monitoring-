from flask import Flask, jsonify
from weather import fetch_weather_data
from db import create_table
from threading import Thread
import time

app = Flask(__name__)
create_table()
latest_weather_data = []

def update_weather_data(interval = 300):
    global latest_weather_data
    while True:
        latest_weather_data = fetch_weather_data()
        print("Database Updated")
        time.sleep(interval)

@app.route('/', methods=['GET'])
def get_weather():
    return jsonify(latest_weather_data)

def run_flask():
    app.run(debug=True)

if __name__ == '__main__':
    update_thread = Thread(target=update_weather_data)
    update_thread.daemon = True
    update_thread.start()
    run_flask()
