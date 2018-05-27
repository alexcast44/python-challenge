# -*- coding: utf-8 -*-
"""
Created on Sat May 26 14:51:45 2018

@author: link3
"""

import os
import csv

csvfile = open('election_data_1.csv')
    
readCSV = csv.reader(csvfile)
#outputfile = open('filename', 'w')
next(readCSV, None)
    
total_count = []

for row in readCSV:
        #print(row)
    total_count.append(row)

csvfile.close()

print("The total number of votes are", len(total_count))

#csv_header = next(csvfile)

#def average(numbers):
#    total = 0
#    length = len(numbers)
#    total: 0.0
    

candidate_names = ['Vestal', 'Torres', 'Seth', 'Cordin']
candidate_set = set(candidate_names)
print(candidate_set)






#candidate = {"name": "Vestal", "vote percentage": }  
    
