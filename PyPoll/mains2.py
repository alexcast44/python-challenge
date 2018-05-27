# -*- coding: utf-8 -*-
"""
Created on Sat May 26 19:48:38 2018

@author: link3
"""
import os
import csv

with open('election_data_1.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    total_count = []
    for row in readCSV:
        #print(row)
        total_count.append(row)
    print(len(total_count))
    