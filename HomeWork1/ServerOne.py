import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/zipcode/<country_name>/<city_name>")
def get_zipcode(country_name, city_name):
    # API endpoint to get zip code from city name
    url: str = f"https://api.zippopotam.us/us/{country_name}/" + city_name
    try:
        # Making a GET request to the API
        response = requests.get(url)
        data = response.json()
        zip_code = data["places"][0]["post code"]
        # Make call to server two to get the weather stats         
        response_weather = requests.get(f"http://localhost:9000/weather/{zip_code}")
        data_weather = response_weather.json()
        # Return response in JSON format
        return jsonify({"weather_stats": data_weather})
    except Exception as e:
        print("Err", e)
        # Return error in JSON format
        return jsonify({"error": "Something went wrong"}), 404

if __name__ == '__main__':
    app.run(debug=True)
