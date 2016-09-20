#!/usr/bin/env python
from twython import Twython
import random
import sys
import requests
from bh_secret import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

# Running script without -p does not post Tweet. 
# python tweet.py -p will post to twitter.
post_tweet = False
if len(sys.argv) > 1 and sys.argv[1] == "-p":
    post_tweet = True

# Initializing the twython object.
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def get_random_cat_fact():
	url = 'http://catfacts-api.appspot.com/api/facts'
	headers = {'Content-Type': 'application/json'}
	resp = requests.get(url, headers)
	cat_fact = resp.json()['facts'][0]
	cat_fact += " #catfacts"
	if len(cat_fact) <= 140:
		return cat_fact
	else:
		return get_random_cat_fact()


# Checks to see if tweet should be printed or posted to twitter
if post_tweet:
	twitter.update_status(status=get_random_cat_fact())
else:
	print (get_random_cat_fact())
