#import necessary modules
import csv
import os

with open(os.path.join("Resources","budget_data.csv"))as f:
  data = csv.reader(f)
  for row in data:
        print(row)