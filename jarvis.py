import datetime
import smtplib
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# sapi5 for windows voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # Inbuilt voices
# print(voices[1].id)                  # optional
engine.setProperty('voices', voices[0].id)


def speak(audio):
    # pass
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else: speak("Good Evening !")
    speak(" I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r= sr.Recognizer()  # recogniser() is a class
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query




def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehio()
    server.starttls()
    server.login('youremail#gmail.com', 'your-r password')
    server.sendEmail('')



if __name__ == "__main__":
    # Output Section
    # speak("Vivek is a good Programmer")
    wishMe()

    while True:
        query = takeCommand().lower()  # to lowercase input speech

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query= query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 10)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        # elif 'play music' in query:
        #    music_dir = "C:\Users\ASUS-PC\Videos\Alan Walker & Ava Max - Alone, Pt. II.mp4"
           # songs = os.listdir(music_dir)
           # print(songs)
           # os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir. the time is {strTime}")

        elif 'open code' in query:
            codePath ="D:\jarvisAI\jarvis.py"
            os.startfile(codePath)

        elif 'email to vivek' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "vivek97921@gail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye! Have a nice day.")
            break  # Exit the loop


    # set Reminders (takes)
    #create dic to mail called name
