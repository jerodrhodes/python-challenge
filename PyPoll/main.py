import os
import csv

# path for file
election_csv = os.path.join("Resources", "election_data.csv")

# lists to store data
voter_id = []
votes = []

# if candidate name in a row is equal to the search add the number of votes
khan_votes = 0
li_votes = 0
correy_votes = 0
otooley_votes = 0

with open(election_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

    #loop through data
    for row in csvreader:
        voter_id.append(row[0])
        votes.append(row[2])

        if (row[2] == "Khan"):
            khan_votes += 1
            

        elif(row[2] == "Li"):
            li_votes += 1
            

        elif(row[2] == "Correy"):
            correy_votes += 1
            
        
        else:
            otooley_votes += 1
            

#total votes
total_votes = len(voter_id)

#percentage of total votes per candidate
khan_pct = round((khan_votes / total_votes * 100), 3)
li_pct = round((li_votes / total_votes * 100), 3)
correy_pct = round((correy_votes / total_votes * 100), 3)
otooley_pct = round((otooley_votes / total_votes * 100), 3)

#find the winner
won = max(khan_votes, li_votes, correy_votes, otooley_votes)
if won == khan_votes:
    winner = "Khan"

elif won == li_votes:
    winner = "Li"

elif won == correy_votes:
    winner = "Correy"

else:
    winner = "O'Tooley"


# Final print to terminal
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("----------------------")
print(f"Khan: {khan_pct}% ({khan_votes})")
print(f"Correy: {correy_pct}% ({correy_votes})")
print(f"Li: {li_pct}% ({li_votes})")
print(f"O'Tooley: {otooley_pct}% ({otooley_votes})")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")

#print to txt file for analysis
analysis_txt = os.path.join("analysis", "election_results.txt")
with open(analysis_txt, "w") as txtfile:
    txtfile.write("Election Results" + "\n")
    txtfile.write("----------------------" + "\n")
    txtfile.write(f"Total Votes: {total_votes} \n")
    txtfile.write("----------------------" + "\n")
    txtfile.write(f"Khan: {khan_pct}% ({khan_votes}) \n")
    txtfile.write(f"Correy: {correy_pct}% ({correy_votes}) \n")
    txtfile.write(f"Li: {li_pct}% ({li_votes}) \n")
    txtfile.write(f"O'Tooley: {otooley_pct}% ({otooley_votes}) \n")
    txtfile.write("----------------------" + "\n")
    txtfile.write(f"Winner: {winner} \n")
    txtfile.write("----------------------")

# print(winner)
# print to check
# print(total_votes)
# print("Khan " + str(khan_votes))
# print("Li " + str(li_votes))
# print("Correy " + str(correy_votes))
# print("O'Tooley " + str(otooley_votes))
# print("K " + str(khan_pct))

# print("Li " + str(li_pct)"%" + " " + str(li_votes))