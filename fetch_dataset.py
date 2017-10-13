import datadotworld as dw
import numpy as np
import os
import random
from utils import clean

def download_dataframe():
    query = """SELECT does_this_tweet_contain_hate_speech, tweet_text
               FROM twitter_hate_speech_classifier_dfe_a845520"""
    result = dw.query('crowdflower/hate-speech-identification', query)
    df = result.dataframe
    return df

def transform(df):
    df.columns = ['label', 'text']
    df['label'] = df['label'].apply(translate)
    df['text'] = df['text'].apply(clean)
    return df

def translate(label):
    translation = {
        'The tweet contains hate speech': '__label__hate',
        'The tweet uses offensive language but not hate speech': '__label__offensive',
        'The tweet is not offensive': '__label__none'
    }
    return translation[label]

def split(df, treshold=0.8):
    mask = np.random.rand(len(df)) < treshold
    train, test = df[mask], df[~mask] 
    return (train, test) 

if __name__ == '__main__':
    df = download_dataframe()
    df = transform(df)

    os.makedirs('data', exist_ok=True)
    df.to_csv('data/tweets', sep='\t', index=False, header=False)

    train, test = split(df)
    train.to_csv('data/tweets_train', sep='\t', index=False, header=False)
    test.to_csv('data/tweets_test', sep='\t', index=False, header=False)
