import random
from tkinter.ttk import Labelframe

from gtts import gTTS
import playsound
import os
from tkinter import *
from functools import partial
import threading
import sys

global lpn
global lon
global aog
lon = []


def speaktext(ftghv, lang, fn):
    try:
        if fn is None:
            o = gTTS(text=ftghv, lang=lang, slow=False)
            o.save("temp.mp3")
            playsound.playsound('temp.mp3', True)
            os.remove("temp.mp3")
        elif lang is None and fn is None:
            o = gTTS(text=ftghv, lang="en", slow=False)
            o.save("temp.mp3")
            playsound.playsound('temp.mp3', True)
            os.remove("temp.mp3")
        else:
            o = gTTS(text=ftghv, lang=lang, slow=False)
            o.save(fn)
            playsound.playsound(fn, True)
            os.remove(fn)
    except:
        raise Exception("File Name Error")


def chunks(yfyo8udc, jk):
    for andioop in range(0, len(yfyo8udc), jk):
        yield yfyo8udc[andioop:andioop + jk]


def gete(ecdxe):
    global lpn
    lpn = ecdxe.get()
    return


def gete2(eyegd):
    global aog
    aog = eyegd.get()
    return


def al():
    global lpn
    lpn = ""
    fjjfjm = lpn
    while True:
        if lpn != fjjfjm:
            global lon
            lon.insert(0, lpn)
            print(lon)
            fjjfjm = lpn


def r(aog, n):
    def listToString(jjvhjjgtd):
        str1 = " "
        return str1.join(jjvhjjgtd)
    agok = aog
    random.shuffle(n)
    while agok > 0:
        agokj = "Team" + str(agok)
        # Speak: Team Number
        speaktext(agokj, "en", "Temp1.mp3")
        # Speak Names
        xyzh = list(chunks(n, agok))
        print(xyzh)
        print(agok)
        speaktext(listToString(xyzh[agok]), "en", "temp.mp3")
        agok = agok - 1


aog = 2
z = threading.Thread(target=al)
z.daemon = True
z.start()
root = Tk()
root.title("RM1")
root.geometry("448x500")
root.config(bg="grey")
f = Label(root, text='Randomizer Mark 1', font=("Courier", 33)).grid(row=0, column=0, columnspan=2)
x = StringVar()
yh = StringVar()
k = Entry(root, textvariable=x).grid(row=1, column=1)
gete = partial(gete, x)
h = Button(root, command=gete, text='Add Name', font=("Courier", 10)).grid(row=1, column=0)
r = partial(r, aog, lon)
rb = Button(root, text="Randomize", font=("Courier", 44), command=r).grid(row=2, column=0, columnspan=2)
lts = Entry(root, textvariable=yh).grid(row=3, column=1)
gete2 = partial(gete2, yh)
aoglb1 = Button(root, text="Submit", font=("Courier", 10)).grid(row=3, column=0)
root.mainloop()
sys.exit()
