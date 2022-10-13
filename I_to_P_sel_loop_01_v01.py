#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:36:02 2022

@author: johnlangham
"""

def check_BMI_cats(patients, your_list):
    #
    #
    # Check if statement. Assume student could have completely messed 
    # everything up, hence the try
    #
    OK = False
    my_list = [0, 0, 0, 0, 0]
    #
    try:
        #      
        for patient in patients:
            #
            if patient.baseline_BMI < 18.5:
                idx = 0
            elif patient.baseline_BMI < 25:
                idx = 1
            elif patient.baseline_BMI < 30:
                idx = 2 
            elif patient.baseline_BMI < 40:
                idx = 3
            else:
                idx = 4
            #
            my_list[idx] += 1
        #
        if my_list == your_list:
            OK = True
        #
    except:
        print("Sorry - there's some problem with your data. Please fix it and try again")
        return
    #
    if not OK:
        print("Sorry - I don't agree with your results. Please try again")
    else:
        print("Your BMI category counts are correct - Well done!")
    #
#
#