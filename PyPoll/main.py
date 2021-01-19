#import necessary modules
import csv
import os

#Create lists for data
votes = []
candidates = []
county = []


with open(os.path.join("Resources","election_data.csv"))as f:
  data = csv.reader(f)
  

  #total number of votes
  #total votes = len[votes]

  #All candidates
  #candidates = unique.row[2]

  #candidate percentages & votes
  #

  #winner based on popular vote

  #print results

  #output results to csv