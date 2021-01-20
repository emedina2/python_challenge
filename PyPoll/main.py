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


  #print results
print(f"""
  --------------------
  Election Results
  --------------------
  Total Votes: {total_votes}
  ---------------------
""")

for row in candidate_data:
  #print(candidate_data)
  print(f"{candidate_data['Candidate']} : {candidate_data['Percent']} % ({candidate_data['Votes']}) ")



print(f'''
--------------------
Winner: {winner}
--------------------
''')
  #output results to csv

  #["Candidate", "Votes for Candidate", "Percent of Vote"]