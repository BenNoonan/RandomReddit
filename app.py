from flask import Flask, render_template
import requests
import oauth2
import urllib, json
from random import randint
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TEMPLATE_AUTO_RELOAD'] = True

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/funny")
def search():
	r = requests.get('http://reddit.com/r/funny/top/.json', headers = {'User-agent': 'Chrome'})#.read().decode("utf-8")
	reddit_data = json.loads(r.text)
	post_rand = randint(0, 24)
	post_title = reddit_data["data"]["children"][post_rand]["data"]["title"]
	post_source =  reddit_data["data"]["children"][post_rand]["data"]["preview"]["images"][0]["source"]["url"]

  return (post_title + "\n" + post_source)

if __name__ == "__main__":
    app.run()