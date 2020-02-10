#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 23:04:27 2020

@author: brian
"""
fname = input("Enter file:")
if len(fname) < 1 : name = "a.txt"
    #else:   print('Wrong File ')
fh = open(fname)
#Create empty Dict
sender = {}
for line in fh:
    #Strip each line to evaluate
    line = line.strip()
    #Look for lines that start with 'From '
    if not line.startswith('From ' ) : continue
    #Strip out the email address
    words = line.split()
    email = words[1]
    #Add email to Sender Dict
    sender[email] = sender.get(email, 0) + 1
  
#Need to create a maximum loop to find the biggest offender
#Create counter and word variable
bcount = -1
bword = None
#loop through dict key and value to find the largest 
#value with the key
for k,v in sender.items():
    if  v > bcount:
        bword = k
        bcount = v
print (bword, bcount)
   