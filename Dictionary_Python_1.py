from PyDictionary import PyDictionary
from playsound import playsound
from gtts import gTTS
import os

dictionary = PyDictionary()

user = input("Enter a Word : ")

try:
    print(user, "-->", dictionary.meaning(user)["Noun"][0])
    gTTS(text=user + "\n" + dictionary.meaning(user)["Noun"][0], lang='en', slow=False).save(
        "Audio Word Files\\word.mp3")
    playsound("Audio Word Files\\word.mp3")
    os.remove("word.mp3")
except:
    pass

try:
    print(user, "-->", dictionary.meaning(user)["Verb"][0])
    gTTS(text=user + "\n" +dictionary.meaning(user)["Verb"][0], lang='en', slow=False).save(
        "Audio Word Files\\word.mp3")
    playsound("Audio Word Files\\word.mp3")
    os.remove("word.mp3")
except:
    pass
    