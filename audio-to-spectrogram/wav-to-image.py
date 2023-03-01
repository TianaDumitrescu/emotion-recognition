
from email.mime import audio
import os
import glob
import subprocess
import argparse
from typing import Any
from pydub import AudioSegment
from pydub.utils import make_chunks
from scipy.io import wavfile
from matplotlib import pyplot as plt
from PIL import Image
import librosa
import librosa.display

#Plots the images
def waveplot(data, sampling_rate, emotion):
    #plt.figure(figsize=(10, 4))
    #plt.title(emotion, size=20)
    librosa.display.waveshow(data, sr=sampling_rate)
    #plt.show()
    plt.savefig('1.jpg', bbox_inches='tight', pad_inches=0, dpi=100)

def spectogram(data, sampling_rate, emotion):
    x = librosa.stft(data)
    xdb = librosa.amplitude_to_db(abs(x))
    #plt.figure(figsize=(10, 4))
    #plt.title(emotion, size=20)
    librosa.display.specshow(xdb, sr=sampling_rate, x_axis='time', y_axis='hz')
    plt.colorbar()
    plt.savefig('2.jpg', bbox_inches='tight', pad_inches=0, dpi=100)


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
    spectrogram_output_file = file.replace(current_folder, emotion).replace('converted-to-default-wav', 'converted-to-spectrogram-v2').replace("/", "\\").replace('.wav', '.jpg');
    waveplot_output_file = file.replace(current_folder, emotion).replace('converted-to-default-wav', 'converted-to-waveplot').replace("/", "\\").replace('.wav', '.jpg');
    print(spectrogram_output_file)
    print(waveplot_output_file)

    # Gets folder name
    f = file.split("\\")
    new_path = "data-sets/converted-to-spectrogram-v2/" + emotion

    # Creates folder if does not exist
    if not os.path.isdir(new_path):
        os.makedirs(new_path)

    f = file.split("\\")
    new_path = "data-sets/converted-to-waveplot/" + emotion

    # Creates folder if does not exist
    if not os.path.isdir(new_path):
        os.makedirs(new_path)

    data, sr = librosa.load(input_file, sr=None)
    librosa.display.waveshow(data, sr=sr)   
    plt.savefig(waveplot_output_file, bbox_inches='tight', pad_inches=0, dpi=100)
    
    x = librosa.stft(data)
    xdb = librosa.amplitude_to_db(abs(x))
    #plt.figure(figsize=(10, 4))
    #plt.title(emotion, size=20)
    #plt.cla()
    librosa.display.specshow(xdb, sr=sr, x_axis='time', y_axis='hz')
    plt.colorbar()
    plt.savefig(spectrogram_output_file, bbox_inches='tight', pad_inches=0, dpi=100)
    plt.clf();
    #exit()
