#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:58:40 2020

Small program for Field Enineers to know where they are on Productivity
at any time.

@author: Brian Pacheco
"""

# enter info
hours = input ('How many hours did you work? ')
training = input ('How many hours were for Training? ')
calls = input ('How many calls did you close? ')
calls = int(calls)
training = float(training)
hours = float(hours)

# Compute needed calls for period
calls_needed = (hours - training) / 4 * 3
print ('\nYou need at least', calls_needed)

#Results
short = calls_needed - calls
above = calls - calls_needed
if calls_needed > calls:
    print ('\nYou are short by ', short, '\nStill not as bad as David!') 
elif calls_needed < calls:
    print ('Doing good! You are over by', above, '\nTry and create a bigger buffer for more Stars.....')
else:
    print ('Even for the period.')
    

    
