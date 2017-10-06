import datadotworld as dw
import numpy as np
from tweet_utils import clean

if __name__ == '__main__':
    query = """SELECT does_this_tweet_contain_hate_speech, tweet_text
               FROM twitter_hate_speech_classifier_dfe_a845520"""
    results = dw.query('crowdflower/hate-speech-identification', query)
    df = results.dataframe
    df.columns = ['label', 'text']

    conditions = [
        (df['label'] == 'The tweet contains hate speech'),
        (df['label'] == 'The tweet uses offensive language but not hate speech'),
        (df['label'] == 'The tweet is not offensive')]
    choices = ['__label__hate', '__label__offensive', '__label__none']
    df['class'] = np.select(conditions, choices, default='__label__none')
    df['text'] = df['text'].apply(clean)
    df[['class', 'text']].to_csv('data/tweets_davidson_short')
