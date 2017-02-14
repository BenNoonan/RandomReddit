import requests
import json
from random import randint

def parser():
	r = requests.get('http://reddit.com/r/funny/top/.json', headers = {'User-agent': 'Chrome'})#.read().decode("utf-8")
	reddit_data = json.loads(r.text)#r.json()
	post_rand = randint(0, 24)

	#print reddit_data["data"]["children"][post_rand]["data"]["name"]	#x will choosen at random
	post_title = reddit_data["data"]["children"][0]["data"]["title"]
	post_source =  reddit_data["data"]["children"][0]["data"]["preview"]["images"][0]["source"]["url"]

parser()