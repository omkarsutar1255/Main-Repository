import datetime
import time
from pygame import mixer
from gtts import gTTS
try:
    audio = gTTS("its time to do eyes exercise")
    audio.save("eyes.mp3")
    audio = gTTS("its time to drink 250 ml water")
    audio.save("water.mp3")
    audio = gTTS("lets do physical exercises")
    audio.save("physical.mp3")
except Exception as e:
    print("If you don't have eyes.mp3, water.mp3, physical.mp3 files")
    print("connect to internet and run again")

def player(filename):
    mixer.init()
    mixer.music.load(filename)
    mixer.music.set_volume(1)
    mixer.music.play()
    while ("true"):
        print("press 'p' to pause, 'r' to resume,\npress 'e' to stop music")
        querry = input(" ")
        if querry == 'p':
            mixer.music.pause()
        elif querry == 'r':
            mixer.music.unpause()
        elif querry == 'e':
            mixer.music.stop()
            break

while("true"):
    dateSTR = datetime.datetime.now().strftime("%H:%M:%S")
    if dateSTR == ("09:16:00"):
        while("true"):
            time.sleep(840)
            player("eyes.mp3")
            time.sleep(900)
            player("water.mp3")
            while ("true"):
                print("if you drank water then enter 'done'")
                drink = input()
                if drink == ("done"):
                    with open("drinking time.txt", "a") as f:
                        f.write(str([str(datetime.datetime.now())]) + "\n")
                        break
            time.sleep(60)
            player("physical.mp3")

            dateSTR2 = datetime.datetime.now().strftime("%H:%M:%S")
            if dateSTR2 == ("17:00:00"):
                break