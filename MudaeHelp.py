# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:28:31 2020

@author: Kenneth Tang
"""
x = "Mash Kyrielight"
y = [2, 3, 4, 4]
z = ["Mash Kyrielight", "Fou", "IU", "Kumiko Oumae", "Kurisu Makise", "Zero Two", \
"Mikoto Misaka", "Hayase Nagatoro", "Suzuno Kamazuki", "Ai Hayasaka", "Chitoge Kirisaki",\
"Tae Takemi", "Taiga Aisaka", "Kumin Tsuyuri", "Sakura Minamoto"]

def fm(lst):
    for i in z:
        print("$fm " + i)
        
def sort(lst):
    lst.sort()
    for i in lst:
        print(i)

sort(z)