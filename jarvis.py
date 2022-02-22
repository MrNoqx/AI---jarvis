import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('Hello Sir Im Jarvis')
engine.say('How May I Help you?')
engine.runAndWait()

def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='eng')
        print(f"user said: {query}\n")

    except Exception as e:
       #print(e)
       print("say that again please...")
       return "None"
    return query 

    
if __name__=="__main__" :
   wishMe()
   



   

                   

