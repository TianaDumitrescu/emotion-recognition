from csv import field_size_limit
import glob
import os

file_pattern = "data-sets/converted-to-spectrogram/**/*.jpg"
files=glob.glob(file_pattern)

if len(files) == 0:
    print("No files to process.")
    exit()

for file in files:
    input_file = file
    f = input_file.split("\\")
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
    
    input_file = input_file.replace("/", "\\");
    output_file = file.replace(current_folder, emotion).replace('converted-to-spectrogram', 'final-data-set/training').replace("/", "\\");
    copy_command = "xcopy /i /y """ + input_file + """ """ + output_file + "" ""
    os.popen(copy_command)
    
    print("Original file: " + input_file)
    print("New file:      " + output_file)
    print(copy_command)
    print()
    exit()