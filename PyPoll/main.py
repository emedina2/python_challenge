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
i = 0
for keys in candidate_data.items():
  print(f"{candidate_data['Candidate'][i]} : {candidate_data['Percent'][i]} % ({candidate_data['Votes'][i]})")
  i += 1
print(f'''
--------------------
Winner: {winner}
--------------------
''')
  #output results to csv
# Create the path for the filename
data_output = os.path.join("Analysis", "analysis.csv")

# Write data to a .csv file
with open(data_output, "w") as csvfile:
    writer = csv.writer(csvfile)
    # To save specific data input as a row in the csv
    writer.writerow(["row1", "row2"])
 