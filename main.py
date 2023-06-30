

import pyttsx3

engine = pyttsx3.init()

"""VOLUME"""
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

"""RATE"""
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)


"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

names = ['etienne selemani', 'junior shindano', 'franck tshiela', 'roger', 'enoch', 'mardochée']
def reader_name(nameList):
    for name in nameList:
        engine.say(name)

engine.say("Ces personnes peuvent avancer")
reader_name(names)
engine.runAndWait()
engine.stop()