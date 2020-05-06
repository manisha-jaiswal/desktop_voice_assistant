#------------------------Iron Man Jarvis AI Desktop Voice Assistant-----------------------

#pip install pipwin then pipwin install pyaudio for installing pyaudio

import pyttsx3
import datetime
import wikipedia #pip install wikipedia
import webbrowser #default library
import os
import speech_recognition as sr
engine=pyttsx3.init('sapi5') #for taking voices
voices=engine.getProperty('voices')
#print(voices)
#print(voices[1].id) #1 for female voice and 0 for male voice
engine.setProperty('voice',voices[1].id)
def speak(audio):
    #pass
    engine.say(audio)
    engine.runAndWait()
#---------------------------------for wish----------------------------------
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning Mam!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon Mam!")
    else:
        speak("Good Evening Mam!")
    speak("I am Jarvis Mam. Please tell me how may i help you !")
#---------------------for givind command to jevis-----------------------------
def takeCommand():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None" #here none is a string
    return query

if __name__ == '__main__':
    #speak("Manu is a good girl")
    #wishme()
    while True:
        query=takeCommand().lower()
    #logic for executing task based on query

    if 'wikipedia' in query:
        speak("Searching wikipedia.............")
        query=query.replace("wikipedia","")
        results =wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("Youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'open HackerRank' in query:
        webbrowser.open("hackerrank.com")

    elif 'open LinkedIn' in query:
        webbrowser.open("LinkedIn.com")

    elif 'play music' in query:
        music_dir = 'C:\\Users\\MANISHA\\Music\\mysong'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))




