import speech_recognition as sr

def recognize_audio(filename):
    try:
        recognizer = sr.Recognizer()
        with sr.WavFile(f"{filename}.wav") as source:
            audio = recognizer.record(source)
            try:
                return recognizer.recognize_google(audio)
            except Exception as err:
                return ""
    except Exception as err:
        raise Exception("Could not convert to text", err)