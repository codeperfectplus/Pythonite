'''
python programfor convert text to speech
'''
from gtts import gTTS
import os

#Pyhton program for change text to speech
sampletext = input('')
language = 'en'

engine = gTTS(text = sampletext, lang= language, slow= False)

#FIle Be Saved in same folder 
engine.save('welcome1.mp3')
