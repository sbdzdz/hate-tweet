import numpy as np
import random
from keras.layers import Dense, Dropout, Embedding, LSTM, Bidirectional
from keras.models import Sequential
from keras.preprocessing import sequence
from keras.preprocessing.text import one_hot


def read_data(filename, vocabulary_size=10000, split=0.2):
    split = max(1-split, split)
    x_train, y_train, x_test, y_test = [], [], [], []
    with open(filename, 'r') as f:
        for line in f:
            try:
                label, tweet = line.split('\t')
                tweet = tweet.strip()
            except ValueError:
                continue
            if random.random() < split:
                x_train.append(one_hot(tweet, vocabulary_size))
                y_train.append(to_numeric(label))
            else:
                x_test.append(one_hot(tweet, vocabulary_size))
                y_test.append(to_numeric(label))
    return ((x_train, y_train), (x_test, y_test))

def to_numeric(label):
    mapping = {'__label__none': 0, '__label__offensive': 1, '__label__hate': 2}
    return mapping.get(label, 0)

if __name__ == '__main__':
    max_features = 20000
    maxlen = 30
    vocabulary_size = 20000
    batch_size = 32
    path = 'data/tweets'
    (x_train, y_train), (x_test, y_test) = read_data(path)

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
