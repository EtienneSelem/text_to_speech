

import pyttsx3

def configure_engine(engine):
    #Volume
    engine.setProperty('volume', 1.0) #Reglage du volume entre 0 et 1

    #Taux de parole
    engine.setProperty('rate', 125) #Réglage du taux de parole

    #Voix (sélection de la voix féminine)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

def reader_name(nameList):
    engine = pyttsx3.init()
    configure_engine(engine)

    for name in nameList:
        engine.say(name)

    engine.runAndWait()
    engine.stop()

names = ['etienne selemani', 'Becky', 'junior shindano', 'franck tshiela', 'enoch', 'mardochée', 'dorcas']
reader_name(names)