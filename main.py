
import requests
from flask import Flask, render_template, request
import os
app = Flask(__name__)
app.debug = True
API_KEY = os.environ.get('API_KEY')

@app.route('/')
def city():
        if request.method == 'GET':
                city = request.args.get('city')
        if city == None or city == '':
                city = 'Mumbai'

        req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&appid='+API_KEY).json()
        print(req)

        description = req['weather'][0]['description'].upper()
        temperature = req['main']['temp']
        icon = req['weather'][0]['icon']
        icon = 'https://openweathermap.org/img/w/'+ icon +'.png'

        return render_template('city.html', city = city, description = description, temperature = temperature, icon = icon)
if __name__ == '__main__':
   app.run()
