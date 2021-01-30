# Automate the Voice Assistance bot.
'''
Author : Tushar Verma
Date : 05-Jan-2021
'''

# All the required module is import
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import os
import random
import smtplib
import requests
import json
import pyjokes
import randfacts
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


engine = pyttsx3.init('sapi5') # Initalize the speak module
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voice = engine.getProperty('voices') 
engine.setProperty('voices',voice[0].id) # Set the audio to male voice 

# This function is used to speak our jarvis voice
def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

# This function is for greeting according to time
def greet():
    hour = int(datetime.datetime.now().hour) # This module helps to give current hr in int form
    if (hour >= 0 and hour < 12):
        print('Good Moring!')
        speak('Good Moring!')
    elif (hour >= 12 and hour < 18):
        print('Good Afternoon!')
        speak('Good Afternoon!')
    else:
        print('Good Evening!')
        speak('Good Evening!')
    print('\nHello I m Jarvis')
    speak('Hello I m Jarvis')
    print('I m your Voice Assistance.\n')
    speak('I m your voice assistance')
    print('\nWhat Can i do for you ?')
    speak('What Can i do for you')



# This function helps to take user audio through microphone and return string output    
def speechCommand():
    sp = sr.Recognizer()
    with sr.Microphone() as source: # take input from microphone
        print('\nListening...')
        sp.energy_threshold = 1000000  
        sp.adjust_for_ambient_noise(source,1)
        sp.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        audio = sp.listen(source)
    # if an error occur then try and expect will handle 
    try:
        print('Recognizing...')
        query = sp.recognize_google(audio,language='en-in') # Using google recognize to give us query in eng
        print(f'Your request : {query}\n')
    except Exception as e:
        print('\nCan you say that again please')
        return 'None'
    return query

# This function is used to send emails
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# This fucntion is used to get news 
def news():
    url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=c111033eb454441284fd42511f07166c'
    res = requests.get(url).text

    rnews = json.loads(res)
    art = rnews['articles']
    return art
        

# Automate the youtube
def autoYT(query):
    
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com/')
    searchbox = driver.find_element_by_name('search_query')
    searchbox.send_keys(query + Keys.ENTER)

    driver.maximize_window()
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.ID,"img"))).click()

# Automate the Google
def autoGoogle(query):

    driver = webdriver.Chrome()
    driver.get('https://www.google.com/')
    searchbox = driver.find_element_by_name('q')
    searchbox.send_keys(query + Keys.ENTER)
    driver.maximize_window()

# Automate the AnimeSite
def autoAnime(query):
    driver = webdriver.Chrome()
    driver.get('https://animeheaven.ru/')
    searchbox = driver.find_element_by_name('q')
    searchbox.send_keys(query + Keys.ENTER)
    driver.maximize_window()

# Automate Chess Site 
def autoChess():
    driver = webdriver.Chrome()
    driver.get('https://www.chess.com/play/online')

# Automate the Wikipedia
def autoWiki(query):
    driver = webdriver.Chrome()
    driver.get('https://www.wikipedia.org/')
    searchbox = driver.find_element_by_name('search')
    searchbox.send_keys(query + Keys.ENTER)
    driver.maximize_window()

# Speak a joke
def jokes():
    joke = pyjokes.get_joke()
    print('\n Joke : ',joke)
    speak(joke)

# Tell a random fact
def facts():
    fact = randfacts.getFact()
    print('\n Random Fact : ',fact)
    speak(fact)

if __name__ == "__main__":
    greet()
    over = True
    while over:
        query = speechCommand().lower()

    # Logic for executing others query giving to jarvis

        if 'wikipedia' in query:  # Give info from wikipedia for particular query ask
            print('\nWhose wikipedia do you want to search ?')
            speak('whose wikipedia do you want to search')
            query = speechCommand().lower()
            query = query.replace('wikipedia', '')
            autoWiki(query)


        elif 'open youtube' in query:   #  open youtube
            print('\nWhich Video you wnat to play ?')
            speak('Which video you want to play')
            query = speechCommand().lower()
            query = query.replace('open youtube', '')
            print(f'\nPlaying {query} on youtube')
            speak(f'playing {query} on youtube')
            autoYT(query)   
     

        elif 'open google'  in query:   #  open Google
            print('\nWhat do you want to search ?')
            speak('what do you want to search')
            query = speechCommand().lower()
            query = query.replace('open google','')
            autoGoogle(query)
            
            

        elif 'open chess' in query:   #  open Chess site
            autoChess()

        elif 'open anime' in query:   #  open anime site
           print('\nWhich Anime do you want to search ?')
           speak('Which Anime do you want to search')
           query = speechCommand().lower()
           query = query.replace('open anime','')
           autoAnime(query)




        elif 'play music' in query:   #  play music
            music_dir = 'D:/Songs'
            songs = os.listdir('D:/Songs')
            print(songs)
            n = len(songs)
            ranSong = random.randrange(0,n-1)
            os.startfile(os.path.join(music_dir,songs[ranSong]))

        elif 'open code' in query:   #  open vscode
            vscode = "C:/Visual Studio Code/Microsoft VS Code/Code.exe"
            os.startfile(vscode)

        elif 'time' in query:    # It shows current time
            srtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f'Sir, The Time is {srtime}')
            speak(f'Sir, the time is {srtime}')

        elif 'email to harry' in query:   # It will send emails
            try:
                speak("What should I say?")
                content = speechCommand()
                to = "yourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")        

        elif 'quit' in query: # It will quit
            print('Thank you for your time! ')
            speak('Thank you for your time')
            over = False

        elif 'news' in query:  
            newspaper = news()
            for i in newspaper:
                print(f'\nNews Headline : ',i['title'])
                print(f'Url : ',i['url'])
                speak(i['title'])

        elif 'jarvis' in query:
            print('\nI m Listening... ')
            speak('i m listening')


        elif 'joke' in query:
            jokes()


        elif 'fact' in query:
            facts()

