import glob
import subprocess
import os

file_pattern = "data-sets/ravdess/**/*.wav"
files=glob.glob(file_pattern)

if len(files) == 0:
    print("No files to process.")
    exit()

# Creates folders in converted-to-default-wav
for file in files:

    # Gets folder name
    f = file.split("\\")
    new_path = "data-sets/converted-to-default-wav/" + f[1]

    # Creates folder if does not exist
    if not os.path.isdir(new_path):
        os.makedirs(new_path)

for file in files:
    input_file = file
    output_file = file.replace('wav','default.wav').replace('ravdess', 'converted-to-default-wav')
    subprocess.Popen(['ffmpeg', '-i', input_file, output_file])

print("Finished processing files.")