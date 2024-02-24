from sys import path
import pyttsx3 
import requests
from requests.api import head #this is for google engine
import speech_recognition as sr #it is for voice taken from user
import wikipedia #for search in wikipedia
import datetime #it is date time module
import webbrowser #it is a browser module for brusing
import os     #it is for system start
import smtplib #it is for email
import cv2 #camera
import random #for songle paly randomly pick
from requests import get
import pywhatkit as kit #it is for send sms in whatsapp web or search engine type use
import sys #it system module for system software and for whole system 
from wikipedia.wikipedia import languages
import pyjokes #for jokes thhis module is work
import pyautogui #switch window
import time
from PyPDF2 import PdfReader
from translate import Translator
import instaloader
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import wolframalpha
import operator
from gtts import gTTS 
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from pygame import mixer
from englisttohindi.englisttohindi import EngtoHindi
import time
from deep_translator import GoogleTranslator
from playsound import playsound
from pathlib import Path






#Here our terminator say engine
def speak(audio):
    #here we create engine for take input from user
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[3].id)
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',150)
    engine.say(audio)
    engine.runAndWait()

def hindi_audio(text):
    speak("please wait")
    try:
        translated = GoogleTranslator(source='auto', target='hi').translate(text)
        var = gTTS(text = translated,lang = 'hi') 
        var.save('E:\\PROGRAME\\PYTHON\\eng.mp3') 
        playsound('E:\\PROGRAME\\PYTHON\\eng.mp3')
    
    except Exception as e:
        print(e)
    
    
#Here the wish me function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    strTime = datetime.datetime.now().strftime("%H:%M")
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        speak(strTime)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon It's ")
        speak(strTime)    
    else:
        speak("Good Evening")
        speak(strTime)
    speak("I am a gauss Sir . Please tell me how may I help you")
    
#take comand from user by microphone
def takeCommand():
    # It take  microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source,timeout=8,phrase_time_limit=5)

    try:
        print("Rcognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)

        print("say that again please...")
        return "None"
    return query

#Here email mathod
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('sksahilaliking.ind@gmail.com', 'sjgn tfsg ghon ghzt')
    server.sendmail('sksahilali.ind@gmail.com', to, content)
    server.quit()
    
#News methode
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=0905e041ccaf4569a23228e0a84f0f3f'
    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eight","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    speak('you want news in hindi or english')
    lang = takeCommand().lower()
    if lang == 'hindi':
        text = "our news are india, "
        for i in range (len(day)):
            text1 = f"todays {day[i]} news is : {head[i]} "
            text = text+text1
        # print(text)
        text2 =f''' {text} '''
        hindi_audio(text2)

    elif lang == 'english':
        for i in range(len(day)):
            speak(f"todays {day[i]} news is : {head[i]}, ")

            


def reader():
    reader = PdfReader("this pdf.pdf")
    number_of_pages = len(reader.pages)
    # speak("which page you want to read")
    # p_n=int(takeCommand())
    p_n=0
    page = reader.pages[p_n]
    text = page.extract_text()
    return text


def calculate(audio_data):
    try:
        app_id = 'EK8P27-23EKREP598'
        client = wolframalpha.Client(app_id)
        res = client.query(audio_data)
        answer = next(res.results).text
        speak(answer)
    except Exception as e:
        speak('invalid value')
    
def TaskExecution():
    # speak("123")
    wishMe()
    while True:
        query = takeCommand().lower()
        #it is wikipedia seachengine
        if "wikipedia" in query:  # '
            speak("Searching wikipedia...")  # '
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=8)
            speak("According to Wikipedia")
            print("According to Wikipedia",result)
            speak(result)
            
        #open youtube
        # elif "open youtube" in query:  # '
        #     webbrowser.open("youtube.com")
            
        #Open google
        elif "open browser" in query:  # '
            speak("Sir, what should i search on google")
            cm =takeCommand().lower()
            webbrowser.open(f"{cm}")
            
        #Open facebook    
        elif "open facebook" in query:  # '
            webbrowser.open("facebook.com")  
            
        #open twitter    
        elif "open twitter" in query:  # '
            webbrowser.open("twitter.com") 
            
        #Open linkedin    
        elif "open linkedin" in query:  # '
            webbrowser.open("linkedin.com") 
            
        #Open Whatsapp web    
        elif "open whatsapp web" in query:  # '
            webbrowser.open("https://web.whatsapp.com/") 
                         
        #Open stackoverflow
        elif "open stackoverflow" in query:  # '
            webbrowser.open("stackoverflow.com")
            
        #Paly Music
        elif "play music" in query:  # '
            music_dir = "C:\\Users\\sksah\\Desktop\\GAUSS\\music"  # '
            songs = os.listdir(music_dir)
            # print(songs)
            rd = random.choice(songs)
            # for song in songs:
            #     if song.endswith('.mp3'):
            #         os.startfile(os.path.join(music_dir, song))
            os.startfile(os.path.join(music_dir, rd))
            print(songs)
            
        #Whats the time
        elif "time" in query:  # '
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir, the time is {strTime}")
            
                

            
        #Send email function
        elif "email to sahil" in query:  # '
            try:
                speak("what should I say?")
                content = takeCommand().lower()
                to = "sahilali.ind@gmail.com"
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("Sorry my friend sahil bhai, I am not able to send this email")
                
        #exit function
        elif "exit" in query:
            exit()
        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()     
        elif "you can sleep" in query or 'sleep now' in query:
            speak("thanks for using me sir, have a good day.")
            break
        elif "done" in query:
            speak("have good day sir")
            sys.exit()
            
        #introduction of terminator
        elif "who are you" in query:
            speak("Sir, I am gauss I am here to help you")
        elif "who made you" in query:
            speak("Sir, sk sahil ali")    
        elif "hello gauss" in query:
            speak("hello sir i am gauss i am here to help you sir ")
        elif "happy new year" in query:
            speak("same to sir sk sahil ali")     
        elif "i love you" in query:
            speak("I Love You to sir")         
            
        #Open VS Code
        elif "open vs code" in query:
            speak("Opening vs code")
            codespotify = "C:\\Users\\sksah\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codespotify)
            
        #open notepad
        elif "open notepad" in query:
            speak("Opening Notepade")
            notepade = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(notepade)
            
        #to close the software os.system("taskkill /f /im name_of_the_software.exe")    
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe") 
               
        #Open cmd
        elif "open command prompt" in query:
            os.system("start cmd")
            
        #Open camera   
        elif "open camera" in query:
            try:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitkey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()
            except Exception as e:
                print(e)
            
        #ip address of user    
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"your IP adress is {ip}")

        
        #send message in whatsapp web
        #                Syntax
        #kit.sendwhatmsg("+91phone_number", "type message" ,hour,min)    
        #and this hour and min are presentTime+2
        elif "send message" in query:
            try:
                speak("tell me the message...")  # '
                message = takeCommand().lower()
                kit.sendwhatmsg("+919337809365", message, datetime.datetime.now().hour, datetime.datetime.now().minute+2)
            except Exception as e:
                speak(e)
             
        #play song on youtube     
        elif "play song on youtube" in query or "youtube" in query:
            speak("Which you want to listen")
            song=takeCommand().lower()
            kit.playonyt(song)
            
        #Joke    
        elif "tell me a joke" in query or 'joke' in query:
            joke =pyjokes.get_joke()
            speak(joke)
            
        #Set alaram    
        elif "set alarm" in query or 'alarm' in query:
            try:
                nn = int(datetime.datetime.now().hour)
                print(nn)
                if nn == 12:
                    music_dir="C:\\Users\\sksah\\Desktop\\GAUSS\\music" #'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                print(e)
                
        #shutdown the pc      
        # elif "shutdown the system" in query:
        #     os.system("shutdown /s /t 5")
            
        #restart the pc    
        # elif "restart the system" in query:
        #     os.system("shutdown /r /t 5")
            
        #sleep the pc    
        # elif "sleep the system" in query:
        #     os.system("rund1132.exe powrprof.dll,SetSuspendState 0,1,0")   
            
        #Switch window
        elif "switch the window" in query or 'window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt") 
            
        #news
        elif "news" in query:
            speak("please wait sir, feteching the news")
            news()                     

        elif "where i am" in query or "where we are" in query or 'where' in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                print(geo_data)
                city = geo_data['city']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are i {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, due to some issue i am not able to find where we are.")
                pass

        # elif "take screenshot" in query or "take a screenshot" in query:
        #     try:
        #         speak("sir, please tell me the name for this screenshot file")
        #         name = takeCommand.lower()
        #         speak("please sir hold the screen for few seconds, i am taking screenshot")
        #         time.sleep(3)
        #         img = pyautogui.screenshot()
        #         img.save(f"{name}.png")
        #         speak("i am done sir, the screenshot is saved in our main folder, now i an ready for next command")
        #     except Exception as e:
        #         speak("An unexpected error has occurred, Please try again")

        elif "take screenshot" in query or "take a screenshot" in query:

            # generating a random number between 1 
            # to 5 which will represent the time 
            # delay 
            random_time = random.randint(1, 5) 

            # create a time delay using the sleep() 
            # method 
            time.sleep(random_time) 

            # Take the screenshot using screenshot() 
            # method 
            myScreenshot = pyautogui.screenshot() 

            # Save the screenshot shot using current 
            # time as file name. 
            file_name = str(time.time())+".png"
            myScreenshot.save(file_name)

        elif "read pdf" in query:
            speak(reader())
            speak("sir, do you have any other work") 

        elif 'instagram profile' in query or 'profile on instagram' in query:
            speak("sir please enter the user name correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user {name}")
            time.sleep(5)
            speak('sir would you like to download profile picture of this account.')
            condition = takeCommand().lower()
            if 'yes' in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak('i am done sir, profile picture is saved in our main folder. now i am ready')
            else:
                pass
        
        elif 'hide all files' in query or 'hide this folder' in query or 'visible for everyone' in query:
            speak('sir please tell me you want to hide this folder or make it visible to everyone')
            condition = takeCommand().lower()
            if 'hide' in condition:
                os.system('attrib +h /s /d') 
                speak('all file are hide')
            elif 'visible' in condition:
                os.system('attrib -h /s /d')

        elif 'calculate' in query:
            # it is for limite time
            speak('Tell me sir what you want to calculate')
            audio_data = takeCommand().lower()
            calculate(audio_data)

            # it only take to value and one operator as a input
            # my_string = takeCommand().lower()
            # print(my_string)
            # def get_operator_fn(op):
            #     return{
            #         '+' : operator.add,
            #         '-' : operator.sub,
            #         'x' : operator.mul,
            #         'divided' : operator.__truediv__,
            #     }[op]
            # def eval_binary_expr(op1, oper, op2):
            #     op1, op2 = int(op1), int(op2)
            #     return get_operator_fn(oper)(op1, op2)
            # speak("your result is")
            # speak(eval_binary_expr(*(my_string.split())))

        elif 'temperature' in query:
            search = 'temperature in balasore'
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find('div',class_="BNeawe").text
            speak(f"current {search} is {temp}")

        elif 'how' in query:
            speak('I am here to listen you')
            # how = takeCommand().lower()
            how = query
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            # speak(how_to[0].summary)
            hindi_audio(how_to[0].summary)

        elif 'how much power left' in query or 'how much power we have' in query or 'battery' in query:
            import psutil
            battery = psutil.sensors_battery()
            print(battery)
            percentage = battery.percent
            speak(f'sir our system have {percentage} percent battery')

        elif 'check internet speed' in query:
            import speedtest
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"sir we  have {dl} bit per second downloading speed and {up} bit per second uploading speed")

        elif 'send sms' in query:
            # this is premimum version 
            # First we have to register the account on the twilio website
            #this is limited
            from twilio.rest import Client
            account_sid = 'AC8eb6d08cf9ed8c27a1f8a73f07372e4b'
            auth_token = '25a312a2817f2f09fb0b12da32400526'
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body='This is th ship that made the kessel',
                from_='+14159929754',
                to='+919337809365'
            )

        elif 'make call' in query:
            # this is premimum version 
            # First we have to register the account on the twilio website
            #this is limited
            from twilio.rest import Client
            account_sid = 'AC8eb6d08cf9ed8c27a1f8a73f07372e4b'
            auth_token = '25a312a2817f2f09fb0b12da32400526'
            client = Client(account_sid, auth_token)
            message = client.calls.create(
                twiml='<Respnse><Say>This is the second testing message from Gauss side..</Say></Response>',
                from_='+14159929754',
                to='+919337809365'
            )

        elif 'volume up' in query:
            pyautogui.press('volumeup')

        elif 'volume down' in query:
            pyautogui.press('volumedown')

        elif 'volume mute' in query:
            pyautogui.press('volumemute')

            




#main methode
if __name__ == "__main__":
    while True:
        permisssion = takeCommand().lower()
        if 'wake up' in permisssion:
            TaskExecution()
        elif 'shut down now' in permisssion:
            sys.exit()