# Automate News Reader.
 
import requests
import json


def reader(str):
    from win32com.client import Dispatch

    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)



if __name__ == "__main__":
    reader('Today News are')
    url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=c111033eb454441284fd42511f07166c'
    res = requests.get(url).text

    news = json.loads(res)
    art = news['articles']

    for i in art:
        print(f'\nNews Headline : ',i['title'])
        print(f'Url : ',i['url'])
        reader(i['title'])
        




