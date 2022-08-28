import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import wikipedia
import cv2
import random
import requests
import speedtest 
import pyjokes
import sys
import inspect
import pyautogui
import pyaudio

from bs4 import BeautifulSoup
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',175)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    t1=datetime.datetime.now().strftime("%I:%M:%S")
    d1=datetime.datetime.now().strftime("%m/%d/%Y")
    
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak(f"currently time is {t1} and date is {d1}")   
    speak("I am Devil. I am here to help you, Please tell me how may I help you Boss.")

def takeCommand():
    #It takes microphone input from the user 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=300
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower() 

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'tell me joke' in query or 'tell me a joke' in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            speak(My_joke)
            speak("hahahaha")

        elif 'how are you' in query or 'how are you devil ' in query:
            speak("i am fine sir, thankyou for asking... i hope you are also fine...")

        elif 'who are you ' in query:
            speak("i am devil, i am a program, and Mr. Prathamesh created me for his comfort.")

        elif 'who is Prathameh Sahare ' in query or 'who is Prathamesh' in query:
            speak("Mr. Prathamesh is my boss, He created me, he is a legend and he is the best person i have met in this world ")

        elif "i can't see you " in query or "why are you not visible" in query or "where is your body" in query:
            speak("i am a program, i am without form,i have no body and shape")

        elif 'open notepad' in query:
            npath="C:\\WINDOWS\\system32\\notepad.exe"
            speak("opening notepad...")
            os.startfile(npath)
            
        elif 'movies' in query:
            mpath="F:\\movies"
            speak("opening movies... , here are the movies, Please enjoy the movie , sir")
            os.startfile(mpath)

        elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak("opening Google")
   
                        
        elif 'open chrome' in query:
            gcpath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            speak("opening chrome browser...")
            os.startfile(gcpath)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")

        elif 'my ip address' in query:
            ip=get('https://api.ipify.org').text
            speak(f"your ip adress is:{ip}")
            print(speak)

        elif 'play music' in query:
            music_dir = "F:\\songs"
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            print(rd)
            speak(rd)
            os.startfile(os.path.join(music_dir,rd))

        elif 'play song' in query:
            music_dir = "F:\\songs"
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            print(rd)
            speak(rd)
            os.startfile(os.path.join(music_dir,rd))
      

        elif 'the time' in query:
            t1= datetime.datetime.now().strftime("%I:%M:%S")
            d1= datetime.datetime.now().strftime("%m/%d/%Y")
            speak(f"Sir, the time is {t1} and the date is {d1}")
        
        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            speak('Screenshot taken.')
                
        elif 'open camera' in query or 'open the camera' in query:
            speak("opening the camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret , img = cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()    

        elif 'about yourself' in query:
            speak("I am an Artificial Intelligence program which is developed by SP.")
        
        elif 'thank you' in query:
            speak("you are most welcome... sir, ")

        elif 'thanks' in query:
            speak("you are most welcome... sir, ")

        
        elif 'shutdown' in query:
            speak("Do you really want to shutdown")
            reply=takeCommand().lower()
            if "yes" in reply:
                speak("shutting down the laptop , it was nice working with you.")
                os.system('shutdown /s /t 1')
            else:
                break

        elif 'restart' in query:
            speak("Do you really want to restart")
            reply=takeCommand().lower()
            if "yes" in reply:
                speak("restarting the laptop, please wait...")
                os.system('restart /r /t 1')
            else:
                break
