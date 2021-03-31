# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:32:13 2021

@author: VIJAY SANTHOSH
"""

participantnumber = 2
participantdata = []
registeredparticipants = 0
outputfile = open("participantdata.txt","w")
while(registeredparticipants < participantnumber):
    temppartdata = []
    name = input("please enter your name:")
    temppartdata.append(name)
    country = input("please enter your country of origin:")
    temppartdata.append(country)
    age = int(input("please enter your age:"))
    temppartdata.append(age)
    print(temppartdata)
    participantdata.append(temppartdata)
    print(participantdata)
    registeredparticipants = +1