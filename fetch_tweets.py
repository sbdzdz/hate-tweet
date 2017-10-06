import re
import string
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
    translation = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    return tweet.translate(translation)

def remove_urls(tweet):
    template = r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'
    tweet = re.sub(template, '', tweet)
    return tweet

def contract_whitespace(tweet):
    tweet = re.sub("\s\s+", " ", tweet.strip())
    return tweet 

def clean(tweet):
    tweet = remove_hashtags(tweet)
    tweet = remove_mentions(tweet)
    tweet = remove_punctuation(tweet)
    tweet = remove_urls(tweet)
    tweet = contract_whitespace(tweet)
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
                tweets.write("{} {}".format(text, label))
            except tweepy.TweepError:
                continue
