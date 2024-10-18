This is a Flask-based application that fetches and stores weather data from the OpenWeatherMap API for multiple cities, updates it periodically, and displays the data via an API. It also triggers alerts when certain weather conditions exceed predefined thresholds.

Features
  Fetches weather data for multiple cities using OpenWeatherMap API.
  Automatically updates weather data every 5 minutes.
  Stores daily summaries of weather data in a SQLite database.
  Provides an API endpoint (/) to display the latest weather data in JSON format.
  Sends alerts when certain weather conditions exceed specified thresholds

step1:
  Clone the repository:
step2:
  Install required dependencies: You can install dependencies listed in requirements.txt using pip:
  pip install -r requirements.txt

step3:
  Set up the environment variables: Create a .env file in the project root and add your OpenWeatherMap API key:
  API_KEY=your_openweathermap_api_key
  
step3:
  Start the Flask server: Run the Flask application with the following command:
  python app.py
  
This will start the server and also fetch weather data periodically (every 5 minutes) and store it in the SQLite database.
