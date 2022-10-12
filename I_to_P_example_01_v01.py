#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:17:50 2022

@author: johnlangham
"""
#
# I_to_P_example_01_vnn.py
#
# This is stored as py so it can be delivered as byte code
#
# v01 - 1st cut
#
import random
import copy
import math
#
def shuffle(list):
    #
    list_copy = copy.deepcopy(list)
    random.shuffle(list_copy)
    #
    return list_copy
#
#
def random_cities():
    #
    return shuffle(capitals)
#
#
def random_countries():
    #
    return shuffle(countries)
#
#
def good_capitals():
    #
    cities    = random_cities()
    countries = random_countries()
    correct = 0
    for cix in range(len(countries)):
        if capitals[cix] == check_dict[countries[cix]]:
            correct += 1
        #
    #
    return correct
#
#
def k1_tries():
    #
    tries = 1000
    total = 0
    for i in range(tries):
        total += good_capitals()
    #
    return total / tries
#
#
def check_result(result=-1):
    #
    # 
    #
    try:
        if result == 1:
            print("Well done - that is correct!")
        else:
            print("Not quite right - have another go")
    except:
        print("Sorry - there has been a problem checking your answer.",
              "Please try again")
    #
#
#
countries = ["England", "Scotland", "Germany", "France", "Japan", "China", 
             "America", "Spain", "Kyrgyzstan", "Russia", "Australia"]
#
capitals  = ["London", "Edinburgh", "Berlin", "Paris", "Tokyo", "Beijing",
             "Washington", "Madrid", "Bishkek", "Moscow", "Canberra"]
#
check_dict = dict(zip(countries, capitals))    
#
# Calculate theorical (mean) number of correct hits each shuffle
#
# Approach is to find maximum Pr of outcomes. Not independent outcomes
#
# For independent events  P(A n B) = P(A)*P(B). 
# For dependent events    P(A n B) = P(A).P(B) / P(A)
# =>
# P(all correct) = 1/n * 1 / (n - 1) * ... * 1 / 2
# 
# So we calculate all the probabilities for 11 to 1 ... we we don't need to
# obviously 1/11 is the largest. But why not 0?
#
# For 0 its  the intersction of 
# P(! 1 correct), P(! 2 correct), ..., P(! all correct) i.e.
# (1 - 1/n) * (1 - 1 / n(n - 1)) * ... * (1 - 1 / n(n - 1)(n - 2) ... 2)
#
do_experiment = False
if do_experiment:
    mult = 1
    #
    for mix in range(2, 12):
        mult *= (1 - 1 / mix)
        #
        print(mult)
        #
        multa = 1
        multb = 1
    #
    for mix in range(11, 1, -1):
        multa *= mix
        multb *= (1 - 1 / mix)
        #
    print(multb)
    #
    # multb has the lowest probability
    #          
#    
#