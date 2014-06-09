from flask import Flask, render_template
from urllib2 import urlopen
from json import load, dumps
import config

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/feeds/')
def feeds():
	response = urlopen(config.url_byu)
	data_byu = load(response)
	response = urlopen(config.url_ars)
	data_ars = load(response)
	response = urlopen(config.url_suns)
	data_suns = load(response)
	response = urlopen(config.url_usmnt)
	data_usmnt = load(response)
	response = urlopen(config.url_stocks)
	data_stocks = load(response)
 	return render_template('feeds.html', data_byu = data_byu, data_ars = data_ars, data_suns = data_suns, data_usmnt = data_usmnt, data_stocks = data_stocks)

if __name__ == '__main__':
	app.run(debug=True)

