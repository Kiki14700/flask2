from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'sandstone'

@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    parameters = {'q': 'rovanjska', 'appid': '464b8e606097703f41f58b71f890ed3f', 'lang': 'hr', 'units': 'metric'}
    response = requests.get(url, parameters)
    weather = response.json()
    return render_template("index.html", weather = weather, datetime = datetime)

@app.template_filter('datetime')
def fomat_datetime(value, format = '%d.%m.%Y %H:%M'):
    return datetime.fromtimestamp (value).strftime(format) 
