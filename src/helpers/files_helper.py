from os import remove

def clean_files(filename):
    remove(f"{filename}.pcm")
    remove(f"{filename}.wav")
