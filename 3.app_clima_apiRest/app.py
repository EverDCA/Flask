# Web application to display weather for
# various cities using https://openweathermap.org/ weather API

# Importamos las bibliotecas necesarias: Flask para crear la aplicación web
# y requests para realizar solicitudes HTTP a la API de OpenWeatherMap.
from flask import Flask, render_template, request
import requests

# Creamos una instancia de la aplicación Flask.
app = Flask(__name__)

# Tu clave de API de OpenWeatherMap
API_KEY = 'a149fbf2a955c1d0e31d66f1f6760be6'

# Definimos la ruta principal de la aplicación que se ejecuta al acceder a la URL raíz ('/').
@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = []  # Lista vacía para almacenar los datos del clima de cada ciudad.
    if request.method == 'POST':  # Verificamos si la solicitud es de tipo POST, al ingresar envía el formulario.
        ciudad = request.form['ciudad']  # Obtenemos el valor del campo 'ciudad' desde el formulario.
        city_list = [city.strip() for city in ciudad.split(',')]  # Separa por comas las ciudades
        
        # Iteramos sobre cada ciudad de la lista ingresada.
        for city in city_list:
            # Construimos la URL de la solicitud a la API de OpenWeatherMap
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es'
            # Realizamos la solicitud HTTP a la API.
            response = requests.get(url)
            # Verificamos si la respuesta de la API fue exitosa (código de estado 200).
            if response.status_code == 200:
                data = response.json()
                # Extraemos la información del clima relevante y la guardamos en un diccionario.
                weather = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'feels_like': data['main']['feels_like'],
                    'temp_min': data['main']['temp_min'],
                    'temp_max': data['main']['temp_max'],
                    'icon': data['weather'][0]['icon']
                }
                # Agregamos la información del clima de la ciudad a la lista 'weather_data'.
                weather_data.append(weather)
            else:
                # Si la API no devuelve los datos correctamente, agregamos un mensaje de error.
                weather_data.append({'city': city, 'error': 'No se pudo obtener el clima.'})

    # Renderizamos el template HTML y pasamos la lista 'weather_data' como contexto.
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
