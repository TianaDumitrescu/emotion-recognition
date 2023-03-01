
from email.mime import audio
import os
import glob
import subprocess
import argparse
from pydub import AudioSegment
from pydub.utils import make_chunks
from scipy.io import wavfile
from matplotlib import pyplot as plt
from PIL import Image
import librosa
import librosa.display

#Plots the images
def waveplot(data, sampling_rate, emotion):
    plt.figure(figsize=(10, 4))
    plt.title(emotion, size=20)
    librosa.display.waveshow(data, sr=sampling_rate)
    plt.show()

def spectogram(data, sampling_rate, emotion):
    x = librosa.stft(data)
    xdb = librosa.amplitude_to_db(abs(x))
    plt.figure(figsize=(10, 4))
    plt.title(emotion, size=20)
    librosa.display.specshow(xdb, sampling_rate=sampling_rate, x_axis='time', y_axis='hz')
    plt.colorbar()


#Finds path  
file_pattern = "data-sets/converted-to-default-wav/**/*.wav"
files=glob.glob(file_pattern)

if len(files) == 0:
    print("No files to process.")
    exit()

for file in files:
    print(file)
    f = file.split("\\")
    current_folder = f[1]

    file_name = f[2]
    f2 = f[2].split("-")
    emotion_number = f2[2]

    match emotion_number:
      case "01":
        emotion = "neutral"
      case "02":
        emotion = "calm"
      case "03":
        emotion = "happy"
      case "04":
        emotion = "sad"
      case "05":
        emotion = "angry"
      case "06":
        emotion = "fearful"
      case "07":
        emotion = "disgust"
      case "08":
        emotion = "surprised"

    input_file = file.replace("/", "\\");
    spectrogram_output_file = file.replace(current_folder, emotion).replace('ravdess', 'converted-to-spectrogram-v2').replace("/", "\\");
    waveplot_output_file = file.replace(current_folder, emotion).replace('ravdess', 'converted-to-waveplot').replace("/", "\\");
    print(spectrogram_output_file)
    print(waveplot_output_file)

    #splitPath = waveplot_output_file.split("\\")
    #emotion = splitPath[2];
    print(librosa.__version__)

    data, sr = librosa.load("a.wav", sr=None)
    waveplot(data, sr, emotion)

    # find emotion category
    #sort into emotion category
    # find emotion category, use as parameter for imagex


    
    
    #input_file = input_file.replace("/", "\\");
    #training_output_file = file.replace(current_folder, emotion).replace('converted-to-spectrogram', 'final-data-set/training').replace("/", "\\");
    #print (training_output_file)
    exit()