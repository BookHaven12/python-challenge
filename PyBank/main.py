# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
records_path = os.path.join("Resources", "budget_data.csv")  # Input file path
financial_analysis = os.path.join("Analysis", "financial_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0 #total months in the data set
total_net = 0 #net total amount of "Profit/Losses" over the entire period

# Add more variables to track other necessary financial data
net_change_list = []     #open list to store changes
greatest_increase = 0    #variable for greatest increase in profit
increase_date = ""       #date associated with greatest increase in profit
greatest_decrease = 0    #variable for greatest decrease in profit
decrease_date = ""       #date associated with greatest decrease in profit


# Open and read the csv
with open(records_path) as financial_data:
    reader = csv.reader(financial_data, delimiter=',')

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
   
    # Track the total and net change
    total_months +=1 #count the first data row as one month
    total_net = int(first_row[1]) #start total net with the first profit/loss value
    previous_profit = int(first_row[1]) #set variable for net change calculation
      
    # Process each row of data
    for row in reader:
        
        # Track the total
        total_months +=1 #to increment the count for each row by one
        current_profit = int(row[1])
        total_net += current_profit

        # Track the net change
        net_change = current_profit - previous_profit
        net_change_list.append(net_change) #adds the calculated net change to the profit and loss list
        previous_profit = int(row[1]) #assigns current profit/loss value to previous profit for the next calculation
    
        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase:
           greatest_increase = net_change
           increase_date = row[0]  #to store the date associated with the greatest increase

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            decrease_date = row[0] #to store the date associated with the greatest decrease


# Calculate the average net change across the months
average_net_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (f"Financial Analysis\n"
          "----------------------------\n"
          f"Total Months: {total_months}\n"
          f"Total: ${total_net}\n"
          f"Average Change: ${average_net_change:.2f}\n"
          f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n"
          f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")

# Print the output
print(output)

# Write the results to a text file
with open(financial_analysis, "w") as txt_file:
    txt_file.write(output)
