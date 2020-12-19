import os
import csv
file_to_load = os.path.join("Resources", "election_results.csv")

# with open(file_to_load) as election_data:
    
file_to_save=os.path.join("analysis","election_analysis.txt")
   
total_votes = 0

candidate_options=[]

candidate_votes={}

winning_canddiate = ""
winning_count = 0
wining_percentage = 0

with open (file_to_load) as election_data:
    file_reader= csv.reader(election_data)
    headers = (next(file_reader))
    for row in file_reader:
        total_votes +=1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1

with open(file_to_save,"w") as txt_file:
    election_results=(f"Election Results\n-----------------------\nTotal Votes: {total_votes:,d}\n-----------------------\n")
    print (election_results, end="")
    txt_file.write(election_results)
 
    for candidate_name in candidate_votes:
        #this is just to shortern the votes, which was defined upstairs
        votes=candidate_votes[candidate_name]
        vote_percentage=float(votes)/float(total_votes)*100
        candidate_results=(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.\n")
        txt_file.write(candidate_results)

        if (votes>winning_count):
            winning_count=votes
            winning_candidate=candidate_name
            winning_percentage=vote_percentage
    winning_result=(f"The winning candidate is {winning_candidate}. The winning vote is {winning_count:,d}. The winning percentage is {winning_percentage:.2f}%.")
    txt_file.write(winning_result)       

