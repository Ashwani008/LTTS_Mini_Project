import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you!")

def takeCommand():
    #(add doc_string) It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return  query


def sendEmail(to, content):
    #reading the password from pwd.txt
    f = open("pwd.txt", "r")
    p = f.read()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rahuldubey7843@gmail.com', p)
    server.sendmail('rahuldubey7843@gmail.com', to, content)
    server.close()



if __name__ =="__main__":
    wishMe()

    while True:

         query = takeCommand().lower()
         if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

         elif 'open youtube' in query:
            webbrowser.open("youtube.com")

         elif 'open google' in query:
            webbrowser.open("google.com")

         elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

         elif 'open codeforces' in query:
            webbrowser.open("codeforces.com")

         elif 'play music' in query:
            music_dir='D:\\Mymusic'
            songs = os.listdir(music_dir)
            print(songs)
            # selecting ramdom songs
            i = random.randrange(0, len(songs)-1, 1)
            os.startfile(os.path.join(music_dir,songs[i]))

         elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

         elif 'open code' in query:
            #open sublime
            codePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(codePath)

         elif 'send email' in query:
            try:
                dict = {'myself' : 'ashwani26061999@gmail.com', 'ankit' : 'ankitpatra21071998@gmail.com'}

                speak("Whom should you want to send email?")
                name = takeCommand().lower()
                print(f"User said: {name}\n")
                if name in dict:
                    to = dict[name]
                    speak(f"What should I say to {name}?")
                    content = takeCommand()
                    # to = "ashwani26061999@gmail.com"
                    print(content)
                    sendEmail(to, content)
                    speak("Email has been sent!")
                else:
                    speak("That name is not present in your contact")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email")

         # elif 'reminder' in query:


         elif 'thank you' in query:
            speak("Thank you Sir, for giving me an opportunity to help you")
            break

