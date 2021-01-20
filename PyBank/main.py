import os
import csv
import numpy as np

#Designate file as for financial data analysis
budgetdata = os.path.join('Resources','budget_data.csv')

#create index for dates, and values
dates = []
PNL = []
changes = [0]
NextRow = []

#read data from csv file 
with open(budgetdata, 'r') as csvfile:
    budgetdata_csv = csv.reader(csvfile, delimiter=',')
    #read header row
    csv_header = next(budgetdata_csv)
    firstrow = next(budgetdata_csv)
    previous = int(firstrow[1])
    PNL.append(int(firstrow[1]))
    dates.append(firstrow[0])
    totalmonths = 1
    #import data from csv to new list & calculate changes
    for row in budgetdata_csv:
      dates.append(row[0])
      totalmonths += 1
      PNL.append(int(row[1]))
      current = int(row[1])
      change = int(current - previous)
      changes.append(change)
      previous = int(row[1])
    #* The net total amount of "Profit/Losses" over the entire period
total = sum(PNL)
totalchanges = sum(changes)
print(len(changes))
average = int(totalchanges / (totalmonths -1))
average = round(average,2)       
    #* The greatest increase in profits (date and amount) over the entire period
gi = max(changes)
index = changes.index(gi)
MaxMonth = dates[index]     
    #* The greatest decrease in losses (date and amount) over the entire period
gd = min(changes)
index = changes.index(gd)
MinMonth = dates[index]

# Specify the file to write to
data_output = os.path.join("Analysis", "analysis.csv")
# Write data to .csv file
w = open(data_output, "w+")
w.write("Financial Analysis")
w.write("\n-------------------------\n")
w.write(f"Total Months: {totalmonths}\n")
w.write(f"Total: ${total}\n")
w.write(f"Average Change: ${average}\n")
w.write(f"Greatest Increase in Profits: {MaxMonth} (${gi}) \n")
w.write(f"Greatest Decrease in Profits: {MinMonth} (${gd}) \n")
w.close()
#print information from text file in terminal
r = open(data_output, "r")
lines = r.readlines()
for line in lines:
  print(line)
