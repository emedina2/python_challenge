#import necessary modules
import csv
import os
import numpy as np


#Create lists for data
candidates = []
candidate = []
candidatevotes= [] 
votepercent = []
with open(os.path.join("Resources","election_data.csv"))as v:
  poll_data = csv.reader(v, delimiter=",")
  csv_header = next(poll_data)

  for row in poll_data:
    candidate.append(row[2])

#total number of votes
total_votes = int(len(candidate))

#Find All candidates
candidates = np.unique(candidate)

#define function to count votes
def countvotes(x):
    return candidate.count(x)

#Use function to find candidate percentages & votes
for x in range(len(candidates)):
    cv = countvotes(candidates[x])
    candidatevotes.append(cv)
    percent = (cv/total_votes) * 100
    votepercent.append(round(percent,3))

candidate_data = {}
for x in range(len(candidates)):
  candidate_data = {"Candidate": candidates[x], "Votes": candidatevotes[x], "Percent": votepercent[x]}

#winner based on popular vote
maxvote = max(candidatevotes)
index = candidatevotes.index(maxvote)
winner = candidates[index]

# Assign the path for the output file
data_output = os.path.join("Analysis", "analysis.csv")

# Write data to a .csv file
w = open(data_output, "w+")
w.write(f"""
--------------------
Election Results
--------------------
Total Votes: {total_votes}
---------------------
""")
i = 0
for x in range(len(candidates)):
  w.write(f"{candidates[i]} : {votepercent[i]} % ({candidatevotes[i]})\n")
  i += 1
w.write(f'''
--------------------
Winner: {winner}
--------------------
''')
w.close()
#print information from text file in terminal
r = open(data_output, "r")
lines = r.readlines()
for line in lines:
  print(line)