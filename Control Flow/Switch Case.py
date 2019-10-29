1# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:37:20 2019

@author: Switch_Case

Function to convert number into string
"""
def change_data_type(argument):
    switcher = {
            0 : "Zero",
            1 : "one",
            2 : "two",
            3 : "three",
            }
    return switcher.get(argument, "Choose Between 0 to 3")

if __name__ == "__main__":
    x = int(input(''))
    print(change_data_type(x))

