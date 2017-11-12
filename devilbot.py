import tweepy
import os
from time import sleep
import random

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def random_definition():
    try:
        with open('dict.txt') as f:
            definitions = [line.rstrip('\n') for line in f]
            definition = str(random.choice(definitions))

            past_tweets = api.user_timeline('devildefinition', count=60, tweet_mode='extended')

            last_sixty_tweets = [
                tweet.full_text.strip()
                for tweet in past_tweets
            ]

            if definition in last_sixty_tweets:
                print("Duplicate selected. Trying again.")
                return random_definition()
            else:
                # print(definition)
                api.update_status(definition)
    except tweepy.TweepError as e:
        print(e.reason)
        sleep(2)





# tweet()
random_definition()
