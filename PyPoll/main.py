#import necessary modules
import csv
import os
import numpy as np

#Create lists for data
voter = []
candidates = []
candidate = []
candidatevotes= [] 

with open(os.path.join("Resources","election_data.csv"))as v:
  poll_data = csv.reader(v, delimiter=",")
  csv_header = next(poll_data)

  for row in poll_data:
    voter.append(row[0])
    candidate.append(row[2])

#total number of votes
total_votes = int(len(voter))
print(f"The total votes is {total_votes}")

  #All candidates
candidates = np.unique(candidate)
print(f"The Candidates are {candidates}")


  #candidate percentages & votes
for x in range(len(candidates)):
    if candidates == candidate:
        candidatevotes[x] += 1

print(candidatevotes)
  #winner based on popular vote

  #print results

  #output results to csv