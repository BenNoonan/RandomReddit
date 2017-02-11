from flask import Flask, render_template
import requests
import oauth2
import urllib, json
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TEMPLATE_AUTO_RELOAD'] = True


@app.route("/")
def home():
	return render_template('index.html')

@app.route("/json")
def search():
	r = requests.get('http://reddit.com/r/funny/.json?count=25&after=t3_10omtd/', headers = {'User-agent': 'Chrome'})
	data = r.json()
	return str(data)

if __name__ == "__main__":
    app.run()