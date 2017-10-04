import tweepy
from config import keys 

auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
auth.set_access_token(keys['OAUTH_TOKEN'], keys['OAUTH_TOKEN_SECRET'])
api = tweepy.API(auth)

with open('data/ids', 'r') as ids, open('data/tweets', 'w') as tweets:
    for line in ids:
        id, label = line.split(',')
        try:
            text = api.get_status(id).text
            text = text.lower()
            tweets.write("{} {}".format(text, label))
        except TweepError:
            continue
