import os
import csv 

months = []
profit_losses = []
change = []

budget_csv = os.path.join("PyBank","Resources","budget_data.csv")
analysis_file = os.path.join("Pybank","Analysis","data_analysis.txt")

with open(budget_csv) as budget_file:
    csv_reader = csv.reader( budget_file, delimiter = ",")
    csv_header = next(csv_reader)
    
    # counting all of the months and putting all of the profit/losses into a list 
    for rows in csv_reader:
        months.append(rows[0])
        profit_losses.append(rows[1])
    total_months = len(months)
    

    # converting the string values to integers 
    profit_losses_convert = [int(i) for i in profit_losses]

    # calculating the net total of profit/losses over entire period 
    total_profit_losses = sum(profit_losses_convert)

    # finding average changes over the entire period 
    
    # for i in range(len(profit_losses_convert)):
    #     change.append(profit_losses_convert[i+1] - profit_losses_convert[i])
    # print(change)


    # finding the greatest increase in profits 


    # finding the greatest decrease in profits


    # creating a nice print statement to display all the analysis

    display = (
        f"Financial Analysis\n"
        f"------------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit_losses}\n"
        f"Average Change: \n"
        f"Greatest Increase in Profits: \n"
        f"Greatest Decrease in Profits: \n"
    )
    print(display)
    