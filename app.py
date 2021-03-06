from flask import Flask, render_template, abort, redirect, url_for
import requests
from requests.exceptions import HTTPError
import oauth2
import urllib, json
from random import randint
app = Flask(__name__)

app.config['DEBUG'] = True
app.config['TEMPLATE_AUTO_RELOAD'] = True

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/subreddit/<subreddit>")
def post_finder(subreddit):
	r = requests.get('http://reddit.com/r/' + subreddit + '/top/.json', headers = {'User-agent': 'Chrome'})
	reddit_data = json.loads(r.text)

	if 'error' in reddit_data:
		abort(404)
	elif reddit_data["data"]["after"] == None:
		abort(404)

	max_post = len(reddit_data["data"]["children"])
	post_rand = randint(0, max_post)

	post_title = reddit_data["data"]["children"][post_rand]["data"]["title"]
	post_source = "static/img/unavailable_img.png"
	post_desc = "No Description"
	
	if 'preview' in reddit_data["data"]["children"][post_rand]["data"]:
	 	post_source = reddit_data["data"]["children"][post_rand]["data"]["preview"]["images"][0]["source"]["url"]

	if 'selftext' in reddit_data["data"]["children"][post_rand]["data"]:
	 	post_desc = reddit_data["data"]["children"][post_rand]["data"]["selftext"]

	return render_template('random.html', data_title = post_title, data_source = post_source, data_desc = post_desc
	, data_sub = subreddit)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()