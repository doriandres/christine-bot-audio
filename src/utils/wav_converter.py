import wave

def convert_to_wav(filename):
    try:
        with open(f"{filename}.pcm", 'rb') as pcm_file:
            pcm_data = pcm_file.read()
        with wave.open(f"{filename}.wav", mode="wb") as wav_writer:
            wav_writer.setparams((2, 2, 44100, 0, 'NONE', 'NONE'))
            wav_writer.writeframes(pcm_data)
    except Exception as err:
        raise Exception("Could not convert to wav file ", err)