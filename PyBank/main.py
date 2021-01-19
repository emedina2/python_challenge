import os
import csv
import math

#Designate file as for financial data analysis
budgetdata = os.path.join('Resources','budget_data.csv')

#create index for dates, and values
dates = []
PNL = []
changes = []
change = ["Change", 0]
NextRow = []

#read data from csv file 
with open(budgetdata, 'r') as csvfile:
    budgetdata_csv = csv.reader(csvfile, delimiter=',')
    #print(budgetdata_csv)
    ##print(type(budgetdata_csv))

    #read header row
    csv_header = next(budgetdata_csv)
    print(f"Header:{csv_header}")
    
    for row in budgetdata_csv:
    #import data from csv to new list
      dates.append(row[0])
      PNL.append(int(row[1]))
      NextRow.append(int(next(row[1]))
    #* Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    ##Changes between each 
      #if row > 1:
      #currentchange = (PNL - NextRow)
      #print(currentchange)
        #change.append(currentchange)
   # print(change)
  print(dates)
  print(NextRow)
    #count dates
    totalmonths = len(dates)
    
   #display total months
    print(totalmonths)

    #* The net total amount of "Profit/Losses" over the entire period
    #Total Sum of P&L
    total = sum(PNL)
    average = total / totalmonths
    print(f"The total Profit & Loss is {total}")
    print(f"The Average change is {average}")
        
    #* The greatest increase in profits (date and amount) over the entire period
      ##gi = max(change)
      
    #* The greatest decrease in losses (date and amount) over the entire period
      ##gd = min(change)


# Specify the file to write to
output_path = os.path.join("Analysis", "Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')
#print text in csv
  #csvwriter.writerows(dates, PNL, change)
