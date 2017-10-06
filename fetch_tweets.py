import tweepy
from config import keys 
from tweet_utils import clean

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
