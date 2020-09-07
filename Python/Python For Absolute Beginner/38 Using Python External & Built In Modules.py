"""import random           # import modules

random_number = random.randint(0, 5)   # random.randint modules gives random numbers in interger type
print(random_number)

rand = random.random()*25       # random.random means random values between 0 to 1 in float type
print(rand)                  # *25 means it random number between 0 to 25 in float type

lst = ["one","two","tree","four"]
choice = random.choice(lst)      # random.choice is use for string type
print(choice)

from playsound import playsound
playsound('C:\\Users\\dell\\Music\\Playlists\Abhi\\Yeh_Vaada_Raha ___Sanam_ft._Mira.mp3')
"""
from playsound import playsound
from gtts import gTTS
def convert_to_audio(text):
    audio = gTTS(text)
    audio.save("files.mp3")
convert_to_audio("hello world this is omkar sutar")
playsound("files.mp3")

"""import numpy as np
import cv2

cap=cv2.VideoCapture('1 - The One where Monica Gets a New Roomate.mkv')

while(true):
    ret, frame=cap.read()

    cv2.inshow('output',frame)
    if(cv2.waitkey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()"""
