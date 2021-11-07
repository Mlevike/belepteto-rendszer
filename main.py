#!/bin/python3

#Beimportaljuk a szukseges konyvtarakat
import RPi.GPIO as GPIO
import time

#Inicializáljuk a GPIO-t
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Definialjuk a billentyu kiosztast
keypad = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["OK", "0", "CANCEL", "D"]
]

#Definiáljuk a kimeneteket
oszlopok = [4, 17, 27, 22]
sorok = [14, 15, 18, 23]

def Nyitas():
    #Definiáljuk az ajtonyitasert felelo kodot
    GPIO.setup(25, GPIO.OUT)
    GPIO.output(25, 0)
    time.sleep(3)
    GPIO.output(25, 1)

def SzamBeker():
    #Bekonfiguraljuk a gpio allapotokat
    #Kimenetek bekonfigurálása
    for i in oszlopok:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, 0)
    #Bemenetek bekonfigurálása
    for i in sorok:
        GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #Billentyuzet Ki-Bemenetek
    #4 - 1
    #17 - 2
    #27 - 3
    #22 - 4
    #14 - 8
    #15 - 7
    #18 - 6
    #23 - 5
    #1-4 oszlopok
    #5-8 kapcsolt sor kod = ""
        szam = ""
        vanszam = False
    while vanszam == False:
        for i in range(0, 4): #Oszlopok
            GPIO.output(oszlopok[i], 1)
            for j in range (0, 4): #Sorok
                if (GPIO.input(sorok[j]) == 1):
                    szam = keypad[i][j]
                    time.sleep(0.2)
                    if szam == keypad[i][j]:
                        GPIO.output(oszlopok[i], 0)
                        return szam;
                    #GPIO.output(oszlopok[i], 0)
            GPIO.output(oszlopok[i], 0)
#Nyitas()
