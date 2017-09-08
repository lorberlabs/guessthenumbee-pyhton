#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "ö, Ä, é, ß"
print "ć, č, đ, š, ž"


import random
n = random.randint(1, 50)
guess = int(raw_input("Vnesite številko med 1 in 50: "))
while n != "Poizkusite uganiti številko":
    print
    if guess < n:
        print "Vaš številka je prenizka"
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print "Vaša ptevilka je previsoka"
        guess = int(raw_input("Enter an integer from 1 to 99: "))
    else:
        print "Ugotivili ste odlično!"
        break
    print