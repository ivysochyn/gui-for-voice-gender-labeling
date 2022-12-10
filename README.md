# gui-for-voice-gender-labeling

## Description
This application makes the labeling process faster for gender classification.
GUI is made with three buttons:
* Male - classifies record as male and moves it to `<destination-directory>` with next labeling scheme: `<number>_M.wav`
* Female - classifies record as female and moves it to `<destination-directory>` with next labeling scheme: `<number>_K.wav`
* IDK - removes the record from `<source-directory-with-wav>` as it's difficult to determine the gender by provided record.

## Usage
```
python main.py <source-directory-with-wav> <destination-directory>
```

## Dependencies
* Tkinter
* simpleaudio
