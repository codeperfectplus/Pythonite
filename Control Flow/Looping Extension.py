# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:50:04 2019

@author: looping Extension

two iterators for a single looping construct
"""

cars = ['Aston', 'Audi', 'McLearn']
accessories = ['Gps', 'car-repair tool kit']

price = {1: "570000", 2:'68000', 3:'450000', 4:'8900', 5:'4500'}

for index, c in enumerate(cars, start =1):
    print("car: %s Price : %s" %(c, price[index]))
    
for index, a in enumerate(accessories, start =1):
    print('accessory : %s Price: %s' %(a, price[index+len(cars)]))