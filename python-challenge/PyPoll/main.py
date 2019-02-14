# Import modules

import os
import csv

# Establish file path

pollCSV = os.path.join("Resources", "election_data.csv")


# Set up value containers

can_lst = []
can_name = []

vote_con = [0,0,0,0]
vote_pct = [0,0,0,0]
pop_vote = []


# Establish counting variables

total_votes = 0


# Open file
with open(pollCSV, newline="") as poll_data:
    polldata = csv.reader(poll_data, delimiter=",")
    polldata_head = next(polldata)

    # Begin iterations

    for x in polldata:
        total_votes = total_votes + int(x[0])
        can_lst.append(str(x[2]))

        for y in can_lst:
            if y not in can_name:
                can_name.append(y)
            if y == can_name[0]:
                vote_con[0] = vote_con[0] + 1
            elif y == can_name[1]:
                vote_con[1] = vote_con[1] + 1
            elif y == can_name[2]:
                vote_con[2] = vote_con[2] + 1
            elif y == can_name[3]:
                vote_con[3] = vote_con[3] + 1

    vote_pct[0] = round(100*(vote_con[0]/total_votes), 3)
    vote_pct[1] = round(100*(vote_con[1]/total_votes), 3)
    vote_pct[2] = round(100*(vote_con[2]/total_votes), 3)
    vote_pct[3] = round(100*(vote_con[3]/total_votes), 3)

    if vote_con[0] == max(vote_con[0], vote_con[1], vote_con[2], vote_con[3]):
        pop_vote = can_name[0]
    elif vote_con[1] == max(vote_con[0], vote_con[1], vote_con[2], vote_con[3]):
        pop_vote = can_name[1]
    elif vote_con[2] == max(vote_con[0], vote_con[1], vote_con[2], vote_con[3]):
        pop_vote = can_name[2]
    elif vote_con[3] == max(vote_con[0], vote_con[1], vote_con[2], vote_con[3]):
        pop_vote = can_name[3]


# Print results

printout = (f"\nElection Results:\n"
            f"-----------------------------------\n"
            f"Total Votes: {str(total_votes)}\n"
            f"-----------------------------------\n"
            f"Khan: {vote_pct[0]}\n"
            f"Correy: {vote_pct[1]}\n"
            f"Li: {vote_pct[2]}\n"
            f"O'Tooley: {vote_pct[3]}\n"
            f"-----------------------------------\n"
            f"Winner: {pop_vote}\n"
            f"-----------------------------------\n"
            )

            
#printout = month_chng
print(printout)

#Export to Text File

f = open("PyPoll_analysis.txt", "w")
f.write(printout)
f.close()