# twitter downloader
# part of 100DaysOfCode

from twitter_keys import *

import json
import requests
import time

# download tweets from a particular user
# we will hard code the username for now

def download_tweets(screen_name, number_of_tweets):

  api_url = '%s/statuses/user_timeline.json' % base_twitter_url

  params = {
      'screen_name':  screen_name,
      'count':        number_of_tweets,
  }

  # now we have this, we need to send it to twitter

  response = requests.get(api_url, params=params, auth=oauth)

  if response.status_code == 200:
    tweets = json.loads(response.content)
    return tweets

  return None

  # get a list of Tweets
tweet_list = download_tweets('dcuthbert', 100)

if tweet_list is not None:

    # loop over each Tweet and print the date and text
    for tweet in tweet_list:

        print '%s\t%s' % (tweet['created_at'], tweet['text'])

else:

    print '[*] No Tweets retrieved.'
