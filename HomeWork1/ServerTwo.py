from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/weather/<zipcode>', methods=['GET'])
def get_weather(zipcode):
    try:
        api_key = '1006b43ba45997fff501fe0df33639f0'
        base_url = f'http://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid={api_key}&units=Imperial'
        print(base_url)
        response = requests.get(base_url)
        weather_data = response.json()
        print("response", weather_data)
        return json.dumps(weather_data)
    except Exception as e:
        print("Err", e)
        error_message = {
            'error': 'Invalid zipcode or API call failed'
        }
        # Return error in JSON format
        return json.dumps(error_message), 400
if __name__ == '__main__':
    app.run(debug=True, port=9000)
