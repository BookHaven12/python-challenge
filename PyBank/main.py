# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
records_path = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
date = []               #open list
profit_losses = []     #open list
greatest_increase = ["", 0]     #list for date and value
greatest_decrease = ["", 0]     #list for date and value


# Open and read the csv
with open(records_path) as financial_data:
    reader = csv.reader(financial_data, delimiter=',')

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    

    # Track the total and net change
   
    
    # Process each row of data
    for row in reader:
        
        # Track the total
        total_months = total_months + 1

        # Track the net change
        total_net += int(row[1])
            

        # Calculate the greatest increase in profits (month and amount)
        

        # Calculate the greatest decrease in losses (month and amount)



# Calculate the average net change across the months
average_net_change = total_net/total_months

# Generate the output summary
print(f"Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_net_change:.2f}")
# print(f"Greatest Increase in Profits: {}")
# print(f"Greatest Decrease in Profits: {}")

# Print the output


# Write the results to a text file
# with open(file_to_output, "w") as txt_file:
#     txt_file.write(output)

