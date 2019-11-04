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
            4 : "Fout",
            5 : "Five",
            6 : "Six",
            7 : "Seven"
            8 : "Eight"
            9 : "Nine"
            }
    return switcher.get(argument, "Choose Between 0 to 9")

if __name__ == "__main__":
    x = int(input(''))
    print(change_data_type(x))

