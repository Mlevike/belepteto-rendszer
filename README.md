# belepteto-rendszer
Egy vállalati beléptető rendszer megvalósítása Arduino-val/Raspberry Pi-vel. Ez a project a Széchényi István Egyetem GKNB_INTM020	tárgykódú Mikroelektromechanikai rendszerek tantárgyhoz készült. A projectet Márton Levente és Kerekes Dániel készítették.

# A rendszer leírása
A projekt céja egy funkcionális vállalati beléptető rendszer megvalósítása, amely engedélyezi a regisztrált ügyfelek számára a belépést (RFID kártya). A biztonság növelése érdekében az RFID kártya leovasását követően a felkasználónak meg kell adni a saját 4 karakter hosszú PIN kódját. A sikeres belépést relékattogtatással és 16x2-es karakteres LCD kijelzővel szemléltetjük. 
Elfelejtett jelszó esetén igényelhető jelszóemlékeztető küldése előre megadott e-mail címen webes felületen keresztül.

# Felhasznált Hardware elemek
- Raspberry pi 1b rev.2
- 4 csatornás relé (MSP430)
- 16x2-es karakteres LCD kijelzővel
- 4x4-es gomb mátrix
- RFID olvasó (SL040)

# Bekötési rajz

![Mikroelektronika kapcsolási rajz 2 0](https://user-images.githubusercontent.com/55978703/146350365-a7def187-c881-4c02-bb38-5284eb897b92.jpg)

# Funkciók
- Az RFID jogosultságokat egy adatbázis kezeli és tárolja az SD kártyán
- A sikeres belépést a Led mátrix pipával és relé hangsélzéssel jelzi
- Sikertelen belépés esetén a led mátrix piros X-et jelenít meg 
- Elfelejtett jelszó esetén kérhető emlékeztető e-mail webes felületen

# Felhasznált software eszközök
- A teljes program Python nyelven készült (python 3.7)
- pip
- LAMP
- gpio
- max7219 (kijelző vezérlő)
- phpmyadmin
