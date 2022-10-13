#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:36:02 2022

@author: johnlangham
"""

def check_mean_median(asd_df, your_mean, your_median):
    #
    # Assume student could have completely messed 
    # everything up, hence the try
    #
    # Could there be a problem with rounding?
    #
    OK = False
    #
    try:
        #      
        my_mean   = asd_df["age"].mean()
        my_median = asd_df["score"].median()
        #
        OK = (my_mean == your_mean) and (my_median == your_median)
        #
    except:
        print("Sorry - there's some problem with your data. Please fix it and try again")
        return
    #
    if not OK:
        print("Sorry - that's not quite right. Please try again")
    else:
        print("Your answers are correct - Well done!")
    #
#
#