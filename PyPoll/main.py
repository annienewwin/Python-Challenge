import os
import csv 

election_csv = os.path.join( "PyPoll", "Resources", "election_data.csv" )
analysis_file = os.path.join( "PyPoll", "Resources", "election_analysis.txt" )

with open(election_csv) as election_file:
    csv_reader = csv.reader( election_file, delimiter= "," )
    csv_header = next( csv_reader ) 

    # finding the total number of votes


    # complete list of candiates who received votes


    # percentage of votes each candiate won


    # total number of votes for each candiate 


    # winner of election 


    # display results 


    # write a txt file with the corresponding results 