# Hate tweet
Detecting hate speech on Twitter.

### Getting the dataset
First, you need to download and configure the data.world package (you can get an API key [here](https://data.world)):
```
pip install datadotworld
dw configure
```
You can now fetch the dataset provided by [Davidson et al. (2017)](https://github.com/t-davidson/hate-speech-and-offensive-language): 
```
python fetch_dataset.py
```
This will create a `data` directory with three files inside: `tweets` (full dataset), `tweets_train` (training set), and `tweets_test` (test set).

### Training the bag-of-tricks model
First, install the Python interface for fastText:
```
pip install cython
pip install fasttext
```
Train the fastText model:
```
python model_fasttext.py
```
This will create a file `classifier.bin` in the `bin/` directory.

### Training the bi-LSTM model
Train the Keras bi-LSTM model:
```
python model_keras.py
```
