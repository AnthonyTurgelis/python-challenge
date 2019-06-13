import os
import csv
import pandas as pd
import numpy as np
from collections import Counter

csvpath = os.path.join('..', 'pypoll', 'election_data.csv')

word_list = ["Khan","Li","O'Toole","Correy"]
count = []
candidates = []
Khan = []
Li = []
Correy = []
Otool = []
word_count = {}.fromkeys(word_list, 0)

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	next(csvfile)
	for row in csvreader:
		count.append(row[2])


for word in word_list:
	candidates.append(word_list.count(word))

totalcan = candidates[0] + candidates[1] + candidates [2] + candidates[3]

print("Election Results")
print("----------------")
print("Total Votes: ", int(len(count)))
print("Khan:", (candidates[0]), 100 * candidates[0] / totalcan, "%")
print("Li:", (candidates[1]), 100 * candidates[1] / totalcan, "%")
print("Correy:", (candidates[2]), 100 * candidates[2] / totalcan, "%")
print("Otool:", (candidates[3]), 100 * candidates[3] / totalcan, "%")
print("I guess everyone is a winner, except for me.")