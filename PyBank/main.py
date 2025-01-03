# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
records_path = os.path.join("Resources", "budget_data.csv")              # Input file path
financial_analysis = os.path.join("Analysis", "financial_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0                                        #to count total months in the data set, initialized to 0
total_net = 0                                           #net total amount of "Profit/Losses" over the entire period

# Add more variables to track other necessary financial data
net_change_list = []                                    #open list to store net_change
greatest_increase = 0                                   #variable to track greatest increase in profit, initialized to 0
increase_date = ""                                      #to store date associated with greatest increase in profit
greatest_decrease = 0                                   #variable to track greatest decrease in profit, initialized to 0
decrease_date = ""                                      #to store date associated with greatest decrease in profit


# Open and read the csv
with open(records_path) as financial_data:
    reader = csv.reader(financial_data, delimiter=',')  #opens the csv file for reading, reads the file as rows split by commas

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)                            #extracts first data row for initialization
   
    # Track the total and net change
    total_months +=1                                    #to count the first data row as one month
    total_net = int(first_row[1])                       #start total net with the first profit/loss value
    previous_profit = int(first_row[1])                 #set variable for net change calculation
      
    # Process each row of data
    for row in reader:                                  #iterates through the rows
        
        # Track the total
        total_months +=1                                #to increment the count for each row by one (adds 1 for each row)
        current_profit = int(row[1])                    #converts current profit/loss to an integer
        total_net += current_profit                     #adds to the running total

        # Track the net change
        net_change = current_profit - previous_profit   #calculate change from the previous month's profit
        net_change_list.append(net_change)              #adds the calculated net change to the profit and loss list
        previous_profit = int(row[1])                   #assigns current profit/loss value to previous profit for the next calculation
    
        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase:              #Compares the calculated net_change to the stored greatest_increase value
           greatest_increase = net_change               #stores the new largest change
           increase_date = row[0]                       #to store the date associated with the greatest increase

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease:              #Compares the calculated net_change to the stored greatest_decrease value
            greatest_decrease = net_change              #stores the new smallest change
            decrease_date = row[0]                      #to store the date associated with the greatest decrease


# Calculate the average net change across the months
average_net_change = sum(net_change_list) / len(net_change_list) #adding all the numbers in the net_change_list then dividing by the amount of numbers

# Generate the output summary
output = (f"Financial Analysis\n"                       #/n is for new line
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
