def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.speak(str)

if __name__ == '__main__':


       import requests
       import json

       url = ('http://newsapi.org/v2/top-headlines?'
              'country=us&'
              'apiKey=9b8a6a83887b4da4ace3d23b91e57e89')
       response = requests.get(url)
       text = response.text
       my_json = json.loads(text)
       for i in range(0,11):
              speak(my_json['article'][i]['title'])