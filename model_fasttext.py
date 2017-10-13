import fasttext
import os

if __name__ == '__main__':
    os.makedirs('bin', exist_ok=True)
    classifier = fasttext.supervised('data/tweets_train', 'bin/classifier')
    result = classifier.test('data/tweets_test')

    print('Precision: {}'.format(result.precision))
    print('Recall: {}'.format(result.recall))
    print('Number of examples: {}'.format(result.nexamples))
