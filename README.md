# belepteto-rendszer
Egy vállalati beléptető rendszer megvalósítása Arduino-val/Raspberry Pi-vel. Ez a project a Széchényi István Egyetem GKNB_INTM020	tárgykódú Mikroelektromechanikai rendszerek tantárgyhoz készült. A projectet Márton Levente és Kerekes Dániel készítették.

# A rendszer leírása
A projekt céja egy funkcionális vállalati beléptető rendszer megvalósítása, amely engedélyezi a regisztrált ügyfelek számára a belépést (RFID kártya). A biztonság növelése érdekében az RFID kártya leovasását követően a felkasználónak meg kell adni a saját 4 karakter hosszú PIN kódját. A sikeres belépést relékattogtatással és 8x8-as led-mátrixxal szemléltetjük. 
Elfelejtett jelszó esetén igényelhető jelszóemlékeztető küldése előre megadott e-mail címen keresztül.

# Felhasznált Hardware elemek
- Raspberry pi 1b rev.2
- 4 csatornás relé (MSP430)
- 8x8-as LED mátrix (MAX7219)
- 4x4-es gomb mátrix
- RFID olvasó (SL040)

# Bekötési rajz

![Mikroelektronika kapcsolási rajz](https://user-images.githubusercontent.com/55978703/140621063-c0fa1787-0edb-4f0d-9545-9185f401b9af.jpg)
