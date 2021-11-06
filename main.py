#!/bin/python3

import RPi.GPIO as GPIO
import time

#Definialjuk a billentyu kiosztast
keypad = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['o', '0', 'c']
]
#Definiáljuk a kimeneteket
oszlopok = [4, 17, 27, 22]
sorok = [14, 15, 18, 23]


def Nyitas():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(25, GPIO.OUT)
    GPIO.output(25, 0)
    time.sleep(3)
    GPIO.output(25, 1)

def KodBeker():
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
    #5-8 kapcsolt sor
    for i in range(0, 3):
        vanszam = false
        oszlop = 0
        sor = 0
#    while vanszam == false:
#        if oszlopok[]
#        if oszlop < 3:
#            oszlop++
Nyitas()
#KodBeker()
