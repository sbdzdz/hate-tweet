# Hate tweet
Detecting hate speech on Twitter.

### Getting the dataset
First, you need to download and configure the data.world package:
```
pip install datadotworld
dw configure
```
Give the API key when prompted (you can get one [here](https://data.world)).

You can now fetch the dataset provided by [Davidson et al. (2017)](https://github.com/t-davidson/hate-speech-and-offensive-language): 
```
python fetch_dataset.py
```
This will create the `data` directory with three files inside: `tweets` (full dataset), `tweets_train` (training set), and `tweets_test` (test set). The split is 80/20, you can change it in `fetch_dataset.py`.

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
