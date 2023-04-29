import pyttsx3                                       # AI Desktop Voice Assistant
import speech_recognition as sr
import datetime                                       # by Zehra
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')    #sapi5 is used to take voices, windows has inbuilt voice we can use it through sapi5
voices = engine.getProperty('voices')
# print(voices[1].id) #there are two voices 
engine.setProperty('voice',voices[1].id)   #to set voices


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour) #hours from 0 to 24
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Abbashu maam,a voice assistant made by Zehra. I am based on artificial intelligence. I take your voice commands and can control your system. what can i do for you")
def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  #seconds of non-speaking audio before a phrase is considered complete 
        # r.adjust_for_ambient_noise(source,duration=1)
        r.energy_threshold = 4000
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)  #harry
        # audio = r.listen(source,timeout=8,phrase_time_limit=8)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query
if __name__=="__main__": 
    wishMe()
    while True:
        query = takeCommand().lower()
    # logic for executing tasks based on query
    if 'wikipedia' in query:

        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentence=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

