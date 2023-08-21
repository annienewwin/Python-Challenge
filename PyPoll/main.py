import os
import csv 

election_csv = os.path.join( "PyPoll", "Resources", "election_data.csv" )
analysis_file = os.path.join( "PyPoll", "Analysis", "election_analysis.txt" )

with open(election_csv) as election_file:
    csv_reader = csv.reader( election_file, delimiter= "," )
    csv_header = next( csv_reader ) 

    vote_count = 0
    candidate_0 = 0
    candidate_1 = 0
    candidate_2 = 0

    candidate_list= []
    candidates = []

    # finding the total number of votes
    for rows in csv_reader:
        vote_count += 1
        candidate_list.append(rows[2])

        # complete list of candidates who received votes
    for i in range(len(candidate_list) -1 ):
        if candidate_list[i+1] != candidate_list[i]:
            candidates.append(candidate_list[i])

    # finding total number of votes and percentage of votes each candidate won
    for i in range(len(candiate_list)):
        if candidate_list[i] == candidates[0]:
            candidate_0 += 1
        elif candidate_list[i] == candidates[1]:
            candidate_1 += 1 
        else:
            candidate_2 += 1

    percentage_0 = round((( candidate_0 / vote_count ) * 100 ),3 )
    percentage_1 = round((( candidate_1 / vote_count ) * 100 ),3 )
    percentage_2 = round((( candidate_2 / vote_count ) * 100 ),3 )

    # winner of election 
    winner = candidates[1]

    # display results 
    display = (
        f"Election Results\n"
        f"------------------------------\n"
        f"Total Votes: {vote_count}\n"
        f"------------------------------\n"
        f"{candidates[0]}: {percentage_0}% ({candidate_0})\n"
        f"{candidates[1]}: {percentage_1}% ({candidate_1})\n"
        f"{candidates[2]}: {percentage_2}% ({candidate_2})\n"
        f"------------------------------\n"
        f"Winner: {winner}\n"
        f"------------------------------\n"
    )

    print(display)

    # write a txt file with the corresponding results 

    with open(analysis_file, "w") as txt_file:
        txt_file.write(display)
