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

@app.route("/<subreddit>")
def post_finder(subreddit):
	r = requests.get('http://reddit.com/r/' + subreddit + '/top/.json', headers = {'User-agent': 'Chrome'})#.read().decode("utf-8")
	reddit_data = json.loads(r.text)
	post_rand = randint(0, 24)

	post_title = reddit_data["data"]["children"][post_rand]["data"]["title"]
	
	if 'preview' in reddit_data["data"]["children"]:
		post_source =  reddit_data["data"]["children"][post_rand]["data"]["preview"]["images"][0]["source"]["url"]
	else:
		post_source = None

	if 'selftext' in reddit_data["data"]["children"]:
		post_desc = reddit_data["data"]["children"][post_rand]["data"]["selftext"]
	else:
		post_desc = None

	return render_template('funny.html', data_title = post_title, data_source = post_source, data_desc = post_desc
	, data_sub = subreddit) 

if __name__ == "__main__":
    app.run()