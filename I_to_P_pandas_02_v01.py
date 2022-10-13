#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:36:02 2022

@author: johnlangham
"""
#
def check_df_subset(asd_df, your_subset_df):
    #
    # Assume student could have completely messed 
    # everything up, hence the try
    #
    import pandas as pd
    #
    OK = False
    #
    try:
        #      
        my_subset_df = asd_df.loc[(asd_df.gender == "f") & (asd_df.development_disorders_in_family == "yes"), "asd":"score"]
        #
        OK = my_subset_df.equals(your_subset_df)
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
