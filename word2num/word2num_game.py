# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:59:35 2021

@author: Gilbert
"""

dicts = {
        "ABCabc": "2",
        "DEFdef": "3",
        "GHIghi": "4",
        "JKLjkl": "5",
        "MNOmno": "6",
        "PQRSpqrs": "7",
        "TUVtuv": "8",
        "WXYZwxyz": "9",
        }

word = input('Input a word:')
output = ''
for letter in word:
    for k,v in dicts.items():
        if letter in k:
            output += v
            break
print(output)

