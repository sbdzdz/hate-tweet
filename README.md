# Hate tweet
Detecting hate speech on Twitter.

### Data collection

Run `fetch_hovy.py` to build a dataset provided by [Zeerak and Hovy (2016)](https://github.com/ZeerakW/hatespeech).

Run `fetch_davidson.py` to build a dataset provided by [Davidson et al. (2017)](https://github.com/t-davidson/hate-speech-and-offensive-language). First, you need to download and configure the data.world package:
```
pip install datadotworld
dw configure
```
Give the API key when prompted (you can get one [here](https://data.world)).

### Training
...
