import os
import csv 

months = []
profit_losses = []
change = []

budget_csv = os.path.join("PyBank","Resources","budget_data.csv")
analysis_file = os.path.join("PyBank","Analysis","budget_analysis.txt")

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
    for i in range(len(months)-1):
        difference = profit_losses_convert[i+1] - profit_losses_convert[i]
        change.append(difference)

    average_change = round(sum(change)/len(change),2)


    # finding the greatest increase in profits 
    greatest_increase = max(change)
    increase_index = change.index(greatest_increase)
    increase_month = months[increase_index + 1]
    

    # finding the greatest decrease in profits
    greatest_decrease = min(change)
    decrease_index = change.index(greatest_decrease)
    decrease_month = months[decrease_index + 1]

    # creating a nice print statement to display all the analysis

    display = (
        f"Financial Analysis\n"
        f"------------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit_losses}\n"
        f"Average Change: ${average_change}\n"
        f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n"
    )
    print(display)
    
    with open(analysis_file, "w") as txt_file:
        txt_file.write(display)