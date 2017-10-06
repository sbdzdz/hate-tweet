import re
import tweepy
from config import keys 

def remove_hashtags(tweet):
    template = r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)" 
    tweet = re.sub(template, '', tweet)
    return tweet

def remove_mentions(tweet):
    template = r'(?:@[\w_]+)'
    tweet = re.sub(template, '', tweet)
    return tweet

def remove_punctuation(tweet):
    pass

def clean(tweet):
    tweet = remove_hashtags(tweet)
    tweet = remove_mentions(tweet)
    return tweet.lower()

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'])
    auth.set_access_token(keys['OAUTH_TOKEN'], keys['OAUTH_TOKEN_SECRET'])
    api = tweepy.API(auth)

    with open('data/ids', 'r') as ids, open('data/tweets', 'w') as tweets:
        for line in ids:
            id, label = line.split(',')
            try:
                tweet = api.get_status(id)
                text = clean(tweet.text)
                tweets.write("{} {}".format(tweet.text, label))
                tweets.write("{} {}".format(text, label))
            except tweepy.TweepError:
                continue
