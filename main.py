#Modules import

import pyttsx3 #installing text to speach module
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

#functions and initialization

MASTER = "Arnab"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0])

#speak out the string which is passed to it...
def speak(text):
    engine.say(text)
    engine.runAndWait()

#this function will greet MASTER According to the time
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour <12:
        speak("Good Moring" + MASTER)

    elif hour>=12 and hour <18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)
    speak("I am Arthur. How may I help You?")

#take commands from MASTER
def takeCommand():

    r = sr.Recognizer

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print(f"user said{query}\n")

    except Exception as e:
        print("Say that again please...")


print("Initializing Arthur...")
speak("Initializing Arthur...")
greet()
takeCommand()