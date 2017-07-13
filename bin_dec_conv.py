#!usr/bin/env python
# -*- coding: utf-8 -*-

# 2014 witti 
# http://www.programmieraufgaben.ch/aufgabe/zahlensystemumrechner-dual-binaer-hexadezimal-und-dezimal/wbc93sou

def bin_dez(zahl):	
	out = 0
	length = len(str(zahl)) - 1
	for i in str(zahl):
		if i != "1" and i != "0":
			print("Falsche Eingabe!")
			quit()		
		if i == "1":
			out = out + 2**length
		length = length - 1
	return out			

def bin_hex(zahl):
	return dez_hex(bin_dez(zahl))

def dez_bin(zahl):
	intzahl = int(zahl)
	out = ""
	while intzahl != 0:
		out = str(intzahl%2)+out
		intzahl = round((intzahl/2)-0.49)
	return out

def dez_hex(zahl):
	intzahl = int(zahl)
	out = ""
	while intzahl != 0:
		if intzahl%16 < 10:
			out = str(intzahl%16)+out
		elif intzahl%16 == 10:
			out = "A"+out
		elif intzahl%16 == 11:
			out = "B"+out
		elif intzahl%16 == 12:
			out = "C"+out
		elif intzahl%16 == 13:
			out = "D"+out
		elif intzahl%16 == 14:
			out = "E"+out
		elif intzahl%16 == 15:
			out = "F"+out
		intzahl = round((intzahl/16)-0.49)
	return out

def hex_dez(zahl):	
	out = 0
	length = len(str(zahl)) - 1
	for i in str(zahl):
		if i != "A" and i != "a" and i != "B" and i != "b" and i != "C" and i != "c" and i != "D" and i != "d" and i != "e" and i != "E" and i != "F" and i != "f" and i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9":
			print("Falsche Eingabe!")
			quit()
		if i == "A" or i == "a":
			out = out + 10*16**length
		elif i == "B" or i == "b":
			out = out + 11*16**length
		elif i == "C" or i == "c":
			out = out + 12*16**length
		elif i == "D" or i == "d":
			out = out + 13*16**length
		elif i == "E" or i == "e":
			out = out + 14*16**length
		elif i == "F" or i == "f":
			out = out + 15*16**length
		elif int(i) < 10:
			out = out + int(i)*16**length
		length = length - 1
	return out

def hex_bin(zahl):
	return dez_bin(hex_dez(zahl))

print("Zahlensystemumrechner")
print("1	Binär		->	Dezimal")
print("2	Binär		->	Hexadezimal")
print("3	Dezimal		->	Binär")
print("4	Dezimal		-> 	Hexadezimal")
print("5	Hexadezimal	->	Dezimal")
print("6	Hexadezimal	->	Binär")
print("Q	Anwendung schließen")

while True:
	menu = str(input("\nBitte wählen sie: "))
	
	if menu == "q" or menu == "Q":
		quit()

	zahl = str(input("Geben sie eine Zahl ein: "))

	if menu == "1":
		out = bin_dez(zahl)
		break
	elif menu == "2":
		out = bin_hex(zahl)
		break
	elif menu == "3":
		out = dez_bin(zahl)
		break
	elif menu == "4":
		out = dez_hex(zahl)
		break
	elif menu == "5":
		out = hex_dez(zahl)
		break
	elif menu == "6":
		out = hex_bin(zahl)
		break

print("\nDas Ergebnis lautet: ", out)
