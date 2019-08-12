import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia  # pip install wikipedia
import webbrowser
import os
from googlesearch import search
import smtplib
import urllib
import json as m_json
import urllib.request
import urllib.parse
import re

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! Sir")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon! Sir")
    else:
        speak("Good Evening! Sir")
    speak("I am Friday. Please tell me how can I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 1000
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Command: {query}\n")

    except Exception as e:
        # print(e)
        print("Unable to recognize, please say again")
       # speak("Unable to recognize, please say again")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()


        # Logic for executing tasks based on query


        if 'what is your name' in query:
            speak('I am Friday,Sir')




        elif 'play music' in query:
            music_dir = 'F:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'who are you' in query:
            speak("I am Friday, Sir your personal assistant.")
        elif 'who is your maker' in query:
            speak("I made by Raj Singha.")
        elif 'open vs code' in query:
            codePath = "C:\\Users\\Raj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Opening VS Code")

        elif 'stop' in query:
            speak("ok")
        elif 'shutdown' in query:
            exit(0)

        elif 'search wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry Sir,I can't find that")

        elif 'what are you doing' in query:
            speak("Sir I am talking with you, and also learning from you")

        elif 'what do you eat' in  query:
            speak("I eat electricity")

        elif 'thank you' and 'nice' in query:
            speak("Its my honour to help you ,Sir")
        elif 'what is your name' and "what's your name" in query:
            speak("Friday Sir")
        elif 'hello' and 'hi' in query:
            speak("yes Sir, I am ready to help")

        elif 'open' in query:
            query = query.replace("open","")
            for url in search(query, stop=1):
                webbrowser.open(url)
                print(url)
                speak("opening"+query)
            print("this line")

