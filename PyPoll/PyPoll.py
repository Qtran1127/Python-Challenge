#Voter ID County Candidate 
import os
import csv 
csvpath = os.path.join('Resources','election_data.csv')
Total_Vote = 0
Received_vote = []
Percentage_Candidate_Won = []
Total_Candidate_Won = []
Election_Winner = []
poll = {}
with open(csvpath,'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread,None)
    for row in csvread: 
        Total_Vote +=1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
    for key, value in poll.items ():
        Total_Candidate_Won.append(key)
        Received_vote.append(value)
    for n in Received_vote:
        Percentage_Candidate_Won.append(round(n/Total_Vote*100,1))
        Clean_data = list(zip(Total_Candidate_Won,Received_vote,Percentage_Candidate_Won))

    for name in Clean_data:
        if max(Received_vote) == name[1]:
            Election_Winner.append(name[0])
winner = Election_Winner[0]
if len(Election_Winner) > 1:
    for w in range(1,len(Election_Winner)):
        winner = winner+", " + Election_Winner[w]
file_num = f"electionvotes.txt"
output_file = os.path.join('Resources','electionvotes' + str(file_num)+'.txt') 

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(Total_Vote) + 
      '\n-------------------------\n')
    for entry in Clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())


