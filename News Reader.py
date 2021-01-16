# Automate News Reader.
 
 '''
Author : Tushar Verma
Date : 20-Dec-2020
 '''
 
import requests
import json


def reader(str):
    from win32com.client import Dispatch

    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)



if __name__ == "__main__":
    reader('Today News are')
    url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=Paste Your Api Key Here'
    res = requests.get(url).text

    news = json.loads(res)
    art = news['articles']

    for i in art:
        print(f'\nNews Headline : ',i['title'])
        print(f'Url : ',i['url'])
        reader(i['title'])
        




