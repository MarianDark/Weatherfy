from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'f4ae3995d2a34ac81574691fcfefb672'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.json.get('city')
    if not city:
        return jsonify({'error': 'No se especificó la ciudad'}), 400

    try:
        response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
        data = response.json()
        if response.status_code == 200:
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].capitalize(),
                'icon': data['weather'][0]['icon']
            }
            return jsonify(weather)
        else:
            return jsonify({'error': data.get('message', 'Error desconocido')}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
