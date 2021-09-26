import speech_recognition as sr
import moviepy.editor as mp
import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'sample.mp4')

clip = mp.VideoFileClip(filename)

clip.audio.write_audiofile(r"converted.wav")

r = sr.Recognizer()

audio = sr.AudioFile("converted.wav")

with audio as source:
  audio_file = r.record(source)
result = r.recognize_google(audio_file)

# exporting the result
with open('recognized.txt',mode ='w') as file:
   file.write("Recognized Speech:")
   file.write("\n")
   file.write(result)
   print("ready!")