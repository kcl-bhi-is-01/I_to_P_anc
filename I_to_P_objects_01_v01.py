#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:36:02 2022

@author: johnlangham
"""

def check_patient_class(Patient):
    #
    # Check mods to patient class
    #
    try:
        #
        #
        #
        results = []
        for BMI in [-1, 0, 7.9, 18.5, 20, 24.9, 25]:
            patient = Patient(260, "M", "C1", 62, BMI, 38.2, 0, 24)
            results.append(patient.risky_BMI())
    except:
        print("Sorry - there's some problem with your Class and / or your method. Please try again")
        return
    #
    if results != [True, True, True, False, False, False, True]:
        print("Sorry - your method is not working correctly. Please try again")
    else:
        print("Your method looks good - Well done!")
    #
#
#