#!/bin/python3
# NEEM TAB HANEM 4 DB SZÓKÖZ!!!
#SSH-N KERESZTÜL NEM MŰKÖDIK !!!
#Beimportaljuk a szukseges konyvtarakat
from __future__ import print_function
import RPi.GPIO as GPIO
import time
import mysql.connector
import RPi_I2C_driver

#Inicialiáljuk LCD-t
mylcd = RPi_I2C_driver.lcd()

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

def KodBeker():
    mylcd.lcd_clear() # Ürítsük a kijelző tartalmát
    mylcd.lcd_display_string("Kerem a kodot:", 1) #Kiirás a kijeltőre
    kod = ""
    csillagok = ""
    while len(kod) < 4:
        time.sleep(0.4)
        szam = SzamBeker()
        if szam != "OK":
            if szam == "CANCEL":
                return "szam"
            else:
                csillagok = csillagok + '*'
                mylcd.lcd_display_string(csillagok, 2)
                kod = kod + szam
                print(szam)
    return kod

#Foprogram
proba = 0
while True:
#Erre lehet hogy majd kell háttérben futó megoldást találni
#Adatok beolvasása
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Kerem a kartyat!", 1)
    id = input()
    print("Kártyabeolvasás megtörtént")
    cnx = mysql.connector.connect(user='phpmyadmin', password='raspberry',
                              host='localhost',
                              database='belepteto')
    mycursor = cnx.cursor()

    sql = "SELECT Password FROM `hitelesítés` WHERE `CardID` =  '" + id + "'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    print("Kodbeker meghívva!")
    jelszo = KodBeker()
    print ("KodBeker meghívva!")
    print (jelszo)
    print ( myresult[0][0])

    if jelszo in myresult[0][0]:
        print('Helyes jelszó :)')
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Helyes jelszo :)", 1)
        proba = 0
        Nyitas()
    else:
        print('Helytelen jelszó :(')
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Rossz jelszo :(", 1)
        time.sleep(1)
        proba = proba+1

    for x in myresult:
        print(x)

    #Nyitjuk az ajtót
    #Nyitas()

    cnx.close()

#jelszó ellenőrzés 
