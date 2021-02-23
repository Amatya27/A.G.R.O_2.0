import pyttsx3
import datetime
import random
import speech_recognition as sr 
import wikipedia 
import webbrowser
import os
import sys
import bs4
import requests
import pyglet
import pyaudio
import googletrans
import warnings
from gtts import gTTS
from time import sleep


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning")
    elif hour >= 12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hello sir, this is AGRO at your service. We are online and ready. How can I assist you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)    
        print("Pardon me sir, please try again...")  
        return "None"
    return query

#____________________________________________________________________

def takeCommanding(x):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language=x)
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)    
        print("Pardon me sir, please try again...")  
        return "None"
    return query
#_____________________________________________________________________

if __name__ == "__main__":
    
    wishMe() 


    while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            #________________________________________________________________
            
            elif 'translate' in query or 'translator' in query:
                print('Sir, which language do you want to speak in?')
                speak('Sir, which language do you want to speak in?')
                x=takeCommand().lower()
                dict1= googletrans.LANGCODES
                try:
                     dict1[x] #print(dict1[x])
                except Exception as e:
                     print("Pardon me sir, the language isn't recognised ...")
                     speak("Pardon me sir, the language isn't recognised. Closing Translator.")
                     #exit()
                     continue
                print('Sir, to which language do you want me to translate it?')
                speak('Sir, to which language do you want me to translate it?')
                b=takeCommand().lower()
                dict1= googletrans.LANGCODES
                try:
                     z=dict1[b] #print(dict1[b])
                except Exception as e:
                     print("Pardon me sir, the language isn't recognised ...")
                     speak("Pardon me sir, the language isn't recognised. Closing Translator. ")
                     #exit()
                     continue

                try:
                    print("Speak in "+x)
                    speak("Speak in "+x)
                    query = takeCommanding(x)
                    #z=dict1[b]
                    from googletrans import Translator
                except ImportError: 
                    print("No module named 'Translator' found") 
                if 'what' in query or 'who' in query or 'where' in query or 'how' in query or 'when' in query or 'which' in query or 'will' in query or 'whom' in query or 'whoose' in query or 'why' in query or 'whether' in query or 'did you' in query:
                        out = query + "?"
                        out = out.replace("translate", "")
                        trans = Translator()
                        t = trans.translate(
                            out, dest=z
                        )
                        print(out)
                        #obj = gTTS(text=t, slow=False, lang= 'fr')
                        print(t.text)
                        tts = gTTS(text=t.text, slow=False, lang=z)
                        filename = 'temp.mp3'
                        tts.save(filename)
                        warnings.filterwarnings("ignore")
                        music = pyglet.media.load(filename, streaming=False)
                        music.play()
                        warnings.filterwarnings("ignore")
                        sleep(music.duration)
                        os.remove(filename)
                        warnings.filterwarnings("ignore")
                        #speak(obj.text)#t.text)  
                else:
                     print(query)
                     query = query.replace("translate", "")
                     trans = Translator()
                     t = trans.translate(
                         query, dest=z
                     )
                     #obj = gTTS(text=t, slow=False, lang= 'fr')
                     print(t.text)
                     tts = gTTS(text=t.text, slow=False, lang=z)
                     filename = 'temp.mp3'
                     tts.save(filename)
                     warnings.filterwarnings("ignore")   
                     music = pyglet.media.load(filename, streaming=False)
                     music.play()
                     warnings.filterwarnings("ignore")
                     sleep(music.duration)
                     os.remove(filename)
                     warnings.filterwarnings("ignore")
                     #speak(obj.text)#t.text) 
            #________________________________________________________________

            elif 'open youtube' in query:
                speak('Opening Youtube...')
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("http://youtube.com")
            
            elif 'developer' in query or 'programmer' in query or 'developed' in query or 'programmed' in query or 'designer' in query or 'creator' in query or 'created' in query:
                 speak('AGRO is an AI Powered Chatbot developed by Amatya Katyayan')
                 print('AGRO is an AI Powered Chatbot developed by Amatya Katyayan')
                 webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://www.linkedin.com/in/amatya-katyayan/")
                 speak('You can know more about Amatya Katyayan using this LinkedIn Page')                

            elif 'open google' in query:
                speak('Opening Google...')
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("http://google.com")
            
            elif 'search' in query or 'updates on' in query or 'update' in query:
                try:
                    from googlesearch import search
                except ImportError: 
                    print("No module named 'google' found") 
                speak('Importing Information and Acquiring relevant data...')
                query = query.replace("search", "")
                for j in search(query, tld="co.in", num=3, stop=3, pause=2):
                    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(str(j))

            elif 'linkedin' in query or 'linked in' in query:
                speak('Opening LinkedIn...')
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://www.linkedin.com/company/cloud-counselage/mycompany/")

            elif 'cloud counselage' in query:
                speak('Opening Homepage...')
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://www.cloudcounselage.com/")

            elif 'mail' in query or 'email' in query:
                speak('Opening Email...')
                webbrowser.open("mailto://hrsupport@cloudcounselage.com")

            elif 'contact' in query:
                speak('Opening Webpage...')
                print('Opening Webpage...')
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://www.cloudcounselage.com/contactus/")
                speak('You can contact us usng any of the options available on the web page.')

            elif 'week 1' in query:
                speak('Opening Week 1 - Basic Training...')
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://cloudcounselage24.bitrix24.com/workgroups/group/180/tasks/task/view/45076/")

            elif 'week 2' in query:
                speak('Opening Week 2 - Advance Training...')
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://cloudcounselage24.bitrix24.com/workgroups/group/180/tasks/task/view/45188/")

            elif 'week 3' in query:
                speak('Opening Week 3 - Proof of Concept [PoC]...')
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://cloudcounselage24.bitrix24.com/workgroups/group/180/tasks/task/view/45308/")

            elif 'week 4' in query:
                speak('Opening Week 4 - Submission...')
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://cloudcounselage24.bitrix24.com/workgroups/group/180/tasks/task/view/45436/")   

            elif 'digital resource library' in query or 'drl' in query:
                speak('Opening Digital Resource Library...')
                webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open("https://cloudcounselage.co.in/#/login")

            elif  'music' in query or 'song' in query:
                music_dir = 'D:\\Songs'
                songs = os.listdir(music_dir)
                n = random.randint(0,len(songs)-1)    
                os.startfile(os.path.join(music_dir, songs[n]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                print(f"Sir, the time is {strTime}")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif 'exit' in query or 'shutdown' in query or 'shut down' in query:
                speak('Lowering power modules and shutting down the system Hope you have a great day sir')
                exit()
        