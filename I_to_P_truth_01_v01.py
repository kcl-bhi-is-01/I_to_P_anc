#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:36:02 2022

@author: johnlangham
"""

def check_patient_truth(patients, patient_ids):
  #
  # Check if statement. Assume student could have completely messed 
  # everything up, hence the try
  #
  OK = False
  selected_ids = []
  #
  try:
    #      
    for patient in patients:
      #
      if patient.gender == "M" and \
      (not(patient.demographic == "D" or patient.demographic == "E") or \
      (patient.baseline_BMI > 25 and patient.baseline_pulse_pressure < 40)):
        #
        selected_ids.append(patient.id)
        #
    #
    # Sets so sequence not a problem
    #
    if set(patient_ids) == set(selected_ids):
        OK = True
    #
  except:
    print("Sorry - there's some problem with your data. Please fix it and try again")
    return
  #
  if not OK:
    print("Sorry - I don't agree with your results. Please try again")
  else:
    print("Correct patients selected - Well done!")
#
#