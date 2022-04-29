from gtts import gTTS
from playsound import playsound
from textblob import TextBlob
import os

word_user = input("Enter Word : ")

with open("words.txt") as f1:
    while(True):
        meaning = f1.readline()

        if(meaning.find(word_user.capitalize() + "  ") == 0):
            print(meaning)
            gTTS(text=meaning, lang='en', slow=False).save(
                "Audio Word Files\\word.mp3")
            playsound("Audio Word Files\\word.mp3")
            os.remove("word.mp3")
            break

        # id the word is not present in the data, we try to correct the word.
        if("Zygote  n" in meaning):
            # spell_check
            word_correct = str(TextBlob(word_user).correct())

            if(word_user != word_correct):
                print("\nCorrect Spelling :", word_correct, "\n")

            # opening data file and running a check again for the corrected word.
            with open("words.txt") as f2:
                while(True):
                    meaning = f2.readline()
                    if(meaning.find(word_correct.capitalize() + "  ") == 0):
                        print(meaning)

                        # generating an audio file
                        gTTS(text=meaning, lang='en', slow=False).save(
                            "Audio Word Files\\word.mp3")
                        playsound("Audio Word Files\\word.mp3")
                        os.remove("word.mp3")
                        break

                    # if both the attempts fail.
                    if("Zygote  n" in meaning):
                        print("Word Not Found")
                        gTTS(text='Word Not Found', lang='en', slow=False).save(
                            "Audio Word Files\\word.mp3")
                        playsound("Audio Word Files\\word.mp3")
                        os.remove("word.mp3")
                        break
            break
