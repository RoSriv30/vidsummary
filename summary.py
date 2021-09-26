import speech_recognition as sr
import moviepy.editor as mp
import requests

def format_summary(summary:str) -> str:
  r'''
  Makes the file output from the summarization API readable for print format 
  Replaces the \n in file with an actual new line character
  Also gets rid of backslashes received by the summary received by the API
  Also deletes id in the beginning of the summary received by the APi, and additional formatting at the end
  '''
  summary = summary.replace('\\n', '\n')
  summary = summary.replace('\\', '')
  pos = 0
  while True:
    pos +=1
    if summary[pos:pos+6] == 'output':
      break
  return summary[pos+10:-4]

filename = 'sample.mp4'

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

# summarize result
r = requests.post(
    "https://api.deepai.org/api/summarization",
    files={
        'text': open('tedtalk.txt', 'rb'),
    },
    headers={'api-key': '13064deb-c7f8-462a-86ef-fef35f0d04b9'}
)

with open('summarized.txt',mode = 'w') as file:
  file.write('Summarized Speech:\n')
  summarized = str(r.json())
  file.write(summarized)

with open('summarized.txt',mode = 'r') as file:
  summary = str(file.readlines())
  summary = format_summary(summary)
  print(summary)

  