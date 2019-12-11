'''
python program in windows 10 for convert text to speech using windows inbuilt feature.

'''

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Text To Speech")