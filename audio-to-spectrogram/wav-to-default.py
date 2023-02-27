import glob

path = "data-sets/ravdess/"
files=glob.glob(path+'**/*.wav')

if len(files)==0:
    print("No files to process.")
    exit

for file in files:
    mp=file
    wa=file.replace('wav','default.wav')
    print(wa)
#subprocess.call(['ffmpeg', mp, '-e', 'mu-law','-r', '16k', wa, 'remix', '1,2'])
print("Finished processing files.")