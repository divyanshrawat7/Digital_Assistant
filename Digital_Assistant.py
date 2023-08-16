import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random
from gtts import gTTS
from datetime import date
import pyjokes
import requests,json
import pywhatkit

from wikipedia.wikipedia import languages

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

mydict={'Dikshant':'deekrawat619@gmail.com',
        'The Wanderers':'thewanderers.addr@gmail.com',
        'Rohit':'rohitgairola7@gmail.com'}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good  Morning  my owner!")

    elif hour>=12 and hour<18:
        speak("Good  Afternoon  my owner!")   

    elif hour>=18 and hour<22:
        speak("Good  Evening  my owner!")
    
    else:
        speak("Greetings my owner! Ohhh!! you haven't sleep yet?")

          
    speak("By the way,I am a digital assistant.") 
def date_time():
    today = date.today()
    fdate = date.today().strftime('%d/%m/%Y')
    speak("  Today's date is: " + fdate)
    strTime = datetime.datetime.now().strftime("%H 'hour' %M 'minute' %S 'seconds'")    
    speak(f"and the time is,{strTime}")

    CITY='Dehradun'
    f=open('openweather.txt', 'r')
    API_KEY=f.read()
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        speak(f"you are at {CITY:-^30}")
        speak(f"Temperature is : {temperature}")
        #speak(f"with Humidity: {humidity}")
        #speak(f"and Pressure: {pressure}")
        #speak(f"if we talk about Weather Report .... it is: {report[0]['description']}")    
        speak('  So .  How may i help you?')  

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing the command!")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Can you please say that again!")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    f=open('gmailpasswd.txt', 'r')
    passwd=f.read()
    server.login('divyanshrawat4@gmail.com',passwd)
    server.sendmail('divyanshrawat4@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    date_time()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching in Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2 )
            speak("According to Wikipedia")
            #print(results)
            speak(results)
            exit()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'match schedule' in query:
            speak("Which team's match schedule you are asking about")
            ze=takeCommand()
            try:
                webbrowser.open(ze," match schedule")
            except Exception as e:
                print(e)
                speak("can't find any match")
        
        elif 'weather' in query:
            speak("Do you want to know about your current location")
            ci=takeCommand()
            if ci=='yes':
                CITY='Dehradun'
                f=open('openweather.txt', 'r')
                API_KEY=f.read()
                BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
                URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
                response = requests.get(URL)
                if response.status_code == 200:
                    data = response.json()
                    main = data['main']
                    temperature = main['temp']
                    humidity = main['humidity']
                    pressure = main['pressure']
                    report = data['weather']
                    speak(f"you are at {CITY:-^30}")
                    speak(f"Temperature is : {temperature}")
                    speak(f"with Humidity: {humidity}")
                    speak(f"and Pressure: {pressure}")
                    speak(f"if we talk about Weather Report .... it is: {report[0]['description']}")    
                    exit()
            else:
                speak("City name please")
                ci=takeCommand()
                CITY='Dehradun'
                f=open('openweather.txt', 'r')
                API_KEY=f.read()
                BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
                URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
                response = requests.get(URL)
                if response.status_code == 200:
                    data = response.json()
                    main = data['main']
                    temperature = main['temp']
                    humidity = main['humidity']
                    pressure = main['pressure']
                    report = data['weather']
                    speak(f"you are at {CITY:-^30}")
                    speak(f"Temperature is : {temperature}")
                    speak(f"with Humidity: {humidity}")
                    speak(f"and Pressure: {pressure}")
                    speak(f"if we talk about Weather Report .... it is: {report[0]['description']}")    
                    exit()

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play' and 'game' in query:
            nu=random.randint(1,100)
            speak('We will play guess the number game')
            speak('Start guessing the number between 1 and 100 including 1 and hundred')
            while True:
                num=takeCommand()
                numb=int(num)
                if numb>nu:
                    speak('guess a number smaller than this')
                    speak("guess again")
                elif numb<nu:
                    speak('guess a number greater than this')
                    speak("guess again")
                elif numb==nu:
                    speak('You won')
                    speak('you guessed the right one')
                    speak('the number is'+nu)
                    exit()
            

        # elif 'play songs' or 'play music' or 'play song' in query:
        #     speak('Want to play it online or offline')
        #     musc=takeCommand()
        #     if musc=='online':
        #         song=query.replace('play','')
        #         #songs=song.replace('online','')
        #         speak('Playing songs for you online')
        #         pywhatkit.playonyt(song)
        #         exit()
        #     elif musc=='offline':
        #         music_dir = 'C:\\Users\\divya\\Downloads\\Songs'
        #         songs = os.listdir(music_dir)
        #         print(songs)    
        #         v=len(songs)
        #         a=int(random.randint(1,v))
        #         os.startfile(os.path.join(music_dir, songs[a]))
        #         exit()
        #     else:
        #         speak("..sorry.. can't play")
        #         exit()


        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'calculation' or 'calculate' or 'solve' in query:
            speak('What do you want to do .... i mean addition.. , substraction.. , etc')
            so=takeCommand()
            if so=="addition" or so=='add':
                speak("how many digits do you want to add?")
                cou=takeCommand()
                cadd=int(cou)
                #ad=[]
                sum=0
                for i in range(cadd):
                    speak("dictate digit number")
                    speak(i+1)
                    dig=takeCommand()
                    digi=int(dig)
                    sum=sum+digi
                speak("The answer is ")
                speak(sum) 
                exit()
            elif so=='subtract' or so=='substraction':
                speak("how many digits do you want to substract?")
                cou=takeCommand()
                cadd=int(cou)
                #ad=[]
                sum=0
                for i in range(cadd):
                    speak("dictate digit number")
                    speak(i+1)
                    dig=takeCommand()
                    digi=int(dig)
                    if i==0:
                        sum=digi
                    else:
                        sum=sum-digi
                speak("The answer is ")
                speak(sum) 
                exit()
            if so=="substraction" or so=='substract' or so=='minus':
                speak("do you want to substract two digits? ")
                cou=takeCommand()
                if cou=='yes':
                    for i in range (2):
                        speak("dictate digit number")
                        speak(i+1)
                        dig=takeCommand()
                        digi=int(dig)
                        sum=sum+digi
                    speak("The answer is ")
                    speak(sum) 
                    exit()       
        elif 'open codechef' in query:
            webbrowser.open("codechef.com")   
        
        # elif 'play music' or 'play songs' or 'play song' in query:
        #     music_dir = 'C:\\Users\\divya\\Downloads\\Songs'
        #     songs = os.listdir(music_dir)
        #     print(songs)    
        #     v=len(songs)
        #     a=int(random.randint(1,v))
        #     os.startfile(os.path.join(music_dir, songs[a]))
        #     exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, {strTime} , is the time right now")
            speak("Do you also want to know about today's date?")
            speak("Say in yes or no")
            da=takeCommand()
            if da=='yes':
                today = date.today()
                fdate = date.today().strftime('%d/%m/%Y')
                speak("Today's date is: " + fdate)
                speak("Have a nice day")
                exit()
            elif da=='no':
                speak('ok , as you wish')
                speak("Have a nice day")
                exit()
        elif 'joke' in query:
            engine.setProperty("rate", 165)
            speak(pyjokes.get_joke())
            exit()       
        elif 'open code' in query:
            codePath = "C:\\Users\\Divyansh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            speak("To whom you want to send a mail")
            con=takeCommand()
            try:
                speak("What should I type in mail?")
                content = takeCommand()
                to = mydict.get(con)    
                sendEmail(to, content)
                speak("Mail has been sent succesfully!")
                speak(" .. Have a nice day")
            except Exception as e:
                print(e)
                speak("Sorry , I am unable to send this email . Can you please try it manually")
                xc=takeCommand()
                if xc=='yes':
                    speak("Ok then")
                    exit()
                elif xc=="no":
                    speak("I can't do it. please try to understand. Some error has occured . So please try it manually")
                    exit()
                else:
                    speak("Answer in yes or no")
                    df=takeCommand()
                    if df=='yes':
                        speak("Ok then")
                        exit()
                    elif df=="no":
                        speak("I can't do it. please try to understand. Some error has occured . So please try it manually")
                        speak("Have a nice day!")
                        exit()
        elif 'exit' or 'thank you' in query:
            speak("Have a nice day!")
            exit()
        else:
            speak("Can you speak that again?")
            print("Can you speak that again?")