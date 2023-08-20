import os
import csv 

profit_losses = []

budget_csv = os.path.join("PyBank","Resources","budget_data.csv")

with open(budget_csv) as budget_file:
    csv_reader = csv.reader( budget_file, delimiter = ",")
    csv_header = next(csv_reader)
    
    # counting all of the months and putting all of the profit/losses into a list 
    for rows in csv_reader:
        profit_losses.append(rows[1])
    print(len(profit_losses))

    # converting the string values to integers 
    profit_losses_convert = [int(i) for i in profit_losses]
    print(profit_losses)

    # calculating the net total of profit/losses over entire period 
    total_profit_losses = sum(profit_losses_convert)
    print(sum_profit_losses)
    
    