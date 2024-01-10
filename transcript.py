import speech_recognition as sr
from os import path
from pydub import AudioSegment

song = input("What's the file name? ")
# convert mp3 file to wav                                                       
sound = AudioSegment.from_mp3(song)
sound.export(song.wav, format="wav")


# transcribe audio file                                                         
AUDIO_FILE = song.wav

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file                  

        print("Transcription: " + r.recognize_google(audio))