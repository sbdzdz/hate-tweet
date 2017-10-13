# Hate tweet
Detecting hate speech on Twitter.

### Data collection

Run `fetch_hovy.py` to build a dataset provided by [Zeerak and Hovy (2016)](https://github.com/ZeerakW/hatespeech). The script uses Twitter API, so you need to put your credentials in `config.py`.

Run `fetch_davidson.py` to build a dataset provided by [Davidson et al. (2017)](https://github.com/t-davidson/hate-speech-and-offensive-language). First, you need to download and configure the data.world package:
```
pip install datadotworld
dw configure
```
Give the API key when prompted (you can get one [here](https://data.world)).

### Training the bag-of-tricks model
First, install fastText:
```
git clone https://github.com/facebookresearch/fastText.git
cd fastText
make
```
Train the classifier:
```
./fasttext supervised -input ../data/train -output hate_speech_model
```
You can test the classifier on the test set:
```
./fasttext test hate_speech_model.bin ../data/test
```
or interactively:
```
./fasttext predict hate_speech_model.bin -
```

### Training the bi-LSTM model
Run ``model.py`` to train the Keras bi-LSTM model. Tweak the input path if necessary.
