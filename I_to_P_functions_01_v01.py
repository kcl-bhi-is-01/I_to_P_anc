#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:17:50 2022

@author: johnlangham
"""
#
# I_to_P_functions_01_vnn.py
#
# This is stored as py so it can be delivered as byte code
#
# v01 - 1st cut
#
def check_primes_function(primes_function):
    #
    # Check primes (up to 1st n) function
    #
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    #
    OK = True
    for n in range(25):
        #
        my_answer   = primes[:n]
        your_answer = primes_function(n)
        #
        if my_answer != your_answer:
            OK = False
            break
        #
    #
    if OK:
        print("Correct - Well done!")
    else:
        print("Sorry - your answer isn't quite right. Have another go")
    #
#
#