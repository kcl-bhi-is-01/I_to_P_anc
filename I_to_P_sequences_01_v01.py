#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:17:50 2022

@author: johnlangham
"""
#
# I_to_P_sequences_01_vnn.py
#
# This is stored as py so it can be delivered as byte code
#
# v01 - 1st cut
#
def check_list_slice(sliced_list):
    #
    # Check sliced list
    #
    my_list      = ["a", 1.3, True, 17, "b", "c", 6.02214076e23, False]
    my_list[3:6] = [-7, "y", "z"]
    #
    answer = my_list[::2]
    #
    if answer == sliced_list:
        print("Correct - Well done!")
    else:
        print("Sorry - your answer isn't quite right. Have another go")
    #
#
#