import os
import csv
import pandas as pd
import numpy as np
import itertools as it

csvpath = os.path.join('..', 'pybank', 'budget_data.csv')

months = []
profit = []
maxi = []
mini = []

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	next(csvfile)
	for row in csvreader:
		months.append(row[0])
		profit.append(int(row[1]))

print("Total Months:", int(len(months)))

totalprofit = sum(profit)
print("Total: $",int(totalprofit))

absolute = np.absolute(profit, out = None)
totalabsolute = sum(absolute)
avgchange = totalabsolute / int(len(months))
print("Average Change: $", avgchange)

max = np.amax(profit)

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	next(csvfile)
	for row in csvreader:
		if float(row[1]) >= (max - 1):
			print("Greatest increase in profits:", row[0], "$",row[1])
			maxi = [row[0],row[1]]

min = np.amin(profit)

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	next(csvfile)
	for row in csvreader:
		if float(row[1]) <= (min + 1):
			print("Greatest decrease in profits:", row[0], "$",row[1])
			mini = [row[0],row[1]]

cleaned_csv = zip(it.repeat(len(months)),it.repeat(float(totalprofit)),maxi,mini)

# Set variable for output file
output_file = os.path.join("budget_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Months","Total","Max Increease","Max Decrease"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
