import os
import csv

#Designate file as for financial data analysis
budgetdata = os.path.join("Resources","budget_data.csv")

#read data from csv file 
with open(budgetdata, 'r') as csvfile:
    budgetdata_csv = csv.reader(csvfile, delimiter=',')
    #print(budgetdata_csv)
    ##print(type(budgetdata_csv))

    #read header row
    csv_header = next(budgetdata_csv)
    print(f"Header:{csv_header}")
    
    for row in budgetdata_csv:
    #create variables for data
      dates = str(row[0])
      print(dates)
      #count dates
      totalmonths = len(dates)
      print(totalmonths)

    #display total months
    #print(totalmonths)

    #* The net total amount of "Profit/Losses" over the entire period
    #Total Sum of P&L

    ##TotalPNL = sum(int(budgetdata_csv[1]))
    ##print(TotalPNL)
    #* Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    ##Changes between each 
    #* The greatest increase in profits (date and amount) over the entire period

    #* The greatest decrease in losses (date and amount) over the entire period