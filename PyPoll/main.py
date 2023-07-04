
ballot_ID= {}
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
output_text = "Election Results\n\n"
output_text += "-------------------------\n\n"
output_text += f"Total Votes: {total_number_votes}\n\n"
output_text += "-------------------------\n\n"
for name,votes in ballot_ID.items():
    perc = votes/total_number_votes*100
    output_text += f"{name}: {round(perc,3)}% ({votes})\n\n"
output_text += "-------------------------\n\n"
votes_list = list(ballot_ID.values())
candidates_list = list(ballot_ID.keys())
highest_vote = max(votes_list)
v_index = votes_list.index(highest_vote)
winner = candidates_list[v_index]
output_text += f"Winner: {winner}\n\n"
output_text += "-------------------------\n\n"
print (output_text)
output_file = open ("PyPoll/analysis/election_data.txt","w")
output_file.write(output_text)
output_file.close()