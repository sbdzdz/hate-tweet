import numpy as np
import random
from keras.layers import Dense, Dropout, Embedding, LSTM, Bidirectional
from keras.models import Sequential
from keras.preprocessing import sequence
from keras.preprocessing.text import one_hot

def read_data(filename, vocabulary_size):
    x, y = [], []
    with open(filename, 'r') as tweets:
        for line in tweets:
            label, tweet = line.split('\t')
            x.append(one_hot(tweet, vocabulary_size))
            y.append(to_numeric(label))
    return (x, y)

def to_numeric(label):
    mapping = {'__label__none': 0, '__label__offensive': 1, '__label__hate': 2}
    return mapping.get(label, 0)

if __name__ == '__main__':
    max_features = 50000
    maxlen = 10
    batch_size = 32
    train = 'data/tweets_train'
    test = 'data/tweets_test'

    x_train, y_train = read_data(train, max_features)
    x_test, y_test = read_data(test, max_features)
    x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
    x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
    y_train = np.array(y_train)
    y_test = np.array(y_test)

    model = Sequential()
    model.add(Embedding(max_features, 128, input_length=maxlen))
    model.add(Bidirectional(LSTM(64)))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))

    model.compile('adam', 'binary_crossentropy', metrics=['accuracy'])

    model.fit(x_train, y_train,
            batch_size=batch_size,
            epochs=30,
            validation_data=[x_test, y_test])
