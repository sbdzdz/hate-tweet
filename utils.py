import re
import string

def remove_hashtags(tweet):
    template = r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)" 
    tweet = re.sub(template, '', tweet)
    return tweet

def remove_mentions(tweet):
    template = r'(?:@[\w_]+)'
    tweet = re.sub(template, '', tweet)
    return tweet

def remove_punctuation(tweet):
    translation = str.maketrans('', '', string.punctuation)
    return tweet.translate(translation)

def remove_urls(tweet):
    template = r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'
    tweet = re.sub(template, '', tweet)
    return tweet

def contract_whitespace(tweet):
    tweet = tweet.replace('\n', ' ')
    tweet = re.sub("\s\s+", " ", tweet.strip())
    return tweet 

def clean(tweet):
    tweet = remove_hashtags(tweet)
    tweet = remove_mentions(tweet)
    tweet = remove_urls(tweet)
    tweet = remove_punctuation(tweet)
    tweet = contract_whitespace(tweet)
    return tweet.lower()

