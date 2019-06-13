cleaned_csv = zip(months,total,average,maxinc,maxdec)

# Set variable for output file
output_file = os.path.join("budget_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Months","Total",""])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
