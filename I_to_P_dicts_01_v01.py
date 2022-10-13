#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:36:02 2022

@author: johnlangham
"""

def check_dictionary(your_dictionary, patients):
    #
    # Assume student could have completely messed 
    # everything up, hence the try
    #
    OK = False
    #
    try:
        #      
        my_dictionary = {}
        for patient in patients:
            my_dictionary[patient.id] = patient
        #
        my_keys   = set(my_dictionary.keys())
        your_keys = set(your_dictionary.keys())
        #
        OK = my_keys == your_keys
        #
        if OK:
            for my_key in my_keys:
                my_pat   = my_dictionary[my_key]
                your_pat = your_dictionary[my_key]
                #
                if my_pat.id != your_pat.id or my_pat.gender != your_pat.gender or \
                   my_pat.demographic != your_pat.demographic or \
                   my_pat.age_at_start !=  your_pat.age_at_start or \
                   my_pat.baseline_BMI !=  your_pat.baseline_BMI or \
                   my_pat.baseline_pulse_pressure != my_pat.baseline_pulse_pressure or \
                   my_pat.outcome != your_pat.outcome or \
                   my_pat.months_to_outcome != your_pat.months_to_outcome:
                    OK = False
                    break
                #
            #
        #
    except:
        print("Sorry - there's some problem with your data. Please fix it and try again")
        return
    #
    if not OK:
        print("Sorry - that's not quite right. Please try again")
    else:
        print("Your dictionary is correct - Well done!")
    #
#
#