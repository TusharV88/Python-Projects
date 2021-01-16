# Automate News Reader.
 
 '''
Author : Tushar Verma
Date : 20-Dec-2020
 '''
 
import requests
import json

# This function used to speak all the news 
def reader(str):
    from win32com.client import Dispatch

    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)



if __name__ == "__main__":
    reader('Today News are')
    # Make sure you have account on newapi.org if not then make one and you can use your api key here to get news
    url = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=Paste Your Api Key Here'
    res = requests.get(url).text  # this make resquest to that site 

    news = json.loads(res)   # get all the news in the json format
    art = news['articles']   # get all the articles from the news

    # This loop is used to print all the titile and url of the news 
    for i in art:
        print(f'\nNews Headline : ',i['title'])
        print(f'Url : ',i['url'])
        reader(i['title'])
        




