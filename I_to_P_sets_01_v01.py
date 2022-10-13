#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:36:02 2022

@author: johnlangham
"""

def check_set_ops(your_intersection, your_union, your_difference, set_1, set_2):
    #
    #
    # Assume student could have completely messed 
    # everything up, hence the try
    #
    OK = False
    #
    try:
        #      
        my_intersection = set_1 & set_2
        my_union        = set_1 | set_2
        my_difference   = set_1 - set_2
        #
        OK = my_intersection == your_intersection and my_union == your_union and \
             my_difference == your_difference
        #
    except:
        print("Sorry - there's some problem with your data. Please fix it and try again")
        return
    #
    if not OK:
        print("Sorry - I don't agree with your results. Please try again")
    else:
        print("Your set operation results are correct - Well done!")
    #
#
#