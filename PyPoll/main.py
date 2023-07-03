ballot_ID = {}
total_number_votes = 0
with open("PyPoll/Resources/election_data.csv", "r") as file:

    header = file.readline()
    for line in file:
        line = line.strip()
        line = line.split (",")
        name = line[2]
        total_number_votes += 1
        if name in ballot_ID:
            ballot_ID[name] += 1
        else:
            ballot_ID[name] = 1

print ("Election Results\n\n")
print("--------------------------\n")
print (f"Total Votes: {total_number_votes}\n\n")
print ("-------------------------\n\n")
for name,votes in ballot_ID.items():
    perc = votes/total_number_votes*100
    print (f"{name}: {round(perc,3)}% ({votes})\n\n")
print ("-------------------------\n\n")
votes_list = list(ballot_ID.values())
candidates_list = list(ballot_ID.keys())
highest_vote = max(votes_list)
v_index = votes_list.index(highest_vote)
winner = candidates_list[v_index]
print (f"Winner: {winner}\n\n")
print ("-------------------------\n\n")

