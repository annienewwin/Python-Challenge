import os
import csv 

election_csv = os.path.join( "PyPoll", "Resources", "election_data.csv" )
analysis_file = os.path.join( "PyPoll", "Analysis", "election_analysis.txt" )

with open(election_csv) as election_file:
    csv_reader = csv.reader( election_file, delimiter= "," )
    csv_header = next( csv_reader ) 

    vote_count = 0
    candiate_0 = 0
    candiate_1 = 0
    candiate_2 = 0

    candiate_list= []
    candiates = []

    # finding the total number of votes
    for rows in csv_reader:
        vote_count += 1
        candiate_list.append(rows[2])

        # complete list of candiates who received votes
    for i in range(len(candiate_list) -1 ):
        if candiate_list[i+1] != candiate_list[i]:
            candiates.append(candiate_list[i])

    # finding total number of votes and percentage of votes each candiate won
    for i in range(len(candiate_list)):
        if candiate_list[i] == candiates[0]:
            candiate_0 += 1
        elif candiate_list[i] == candiates[1]:
            candiate_1 += 1 
        else:
            candiate_2 += 1

    percentage_0 = round((( candiate_0 / vote_count ) * 100 ),3 )
    percentage_1 = round((( candiate_1 / vote_count ) * 100 ),3 )
    percentage_2 = round((( candiate_2 / vote_count ) * 100 ),3 )

    # winner of election 
    winner = candiates[1]

    # display results 
    display = (
        f"Election Results\n"
        f"------------------------------\n"
        f"Total Votes: {vote_count}\n"
        f"------------------------------\n"
        f"{candiates[0]}: {percentage_0}% ({candiate_0})\n"
        f"{candiates[1]}: {percentage_1}% ({candiate_1})\n"
        f"{candiates[2]}: {percentage_2}% ({candiate_2})\n"
        f"------------------------------\n"
        f"Winner: {winner}\n"
        f"------------------------------\n"
    )

    print(display)

    # write a txt file with the corresponding results 

    with open(analysis_file, "w") as txt_file:
        txt_file.write(display)