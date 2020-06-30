import random
from gtts import gTTS
import playsound
import os


def listToString(s):
    str1 = " "
    return str1.join(s)


def speaktext(Text, lang, fn):
    try:
        if fn is None:
            o = gTTS(text=Text, lang=lang, slow=False)
            o.save("temp.mp3")
            playsound.playsound('temp.mp3', True)
            os.remove("temp.mp3")
        elif lang is None and fn is None:
            o = gTTS(text=Text, lang="en", slow=False)
            o.save("temp.mp3")
            playsound.playsound('temp.mp3', True)
            os.remove("temp.mp3")
        else:
            o = gTTS(text=Text, lang=lang, slow=False)
            o.save(fn)
            playsound.playsound(fn, True)
            os.remove(fn)
    except:
        raise Exception("File Name Error")


aog = 3
agok = aog


def chunks(l, jk):
    """Yield successive jk-sized chunks from l."""
    for i in range(0, len(l), jk):
        yield l[i:i + jk]


n = ["Alexander", "Sophie", "Lynn", "John", "Mac", "Tony", "Mac Jr."]
random.shuffle(n)
while agok > 0:
    xyzh = list(chunks(n, aog))
    agokj = "Team" + str(agok)
    # Speak: Team Number
    speaktext(agokj, "en", "Temp1.mp3")
    # Speak Names
    speaktext(listToString(xyzh[agok - 1]), "en", "temp.mp3")
    agok = agok - 1
