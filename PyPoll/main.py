# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
election_csv = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_name = [] #list for candidate names
candidate_votes = {} #dictionary to store votes for each candidate


# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(election_csv) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0                         #add the candidate's name as a key and initialize the vote count to 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1                            #increment the candidate's vote by 1

# Open a text file to save the output
# with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(total_votes)

    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner
   

        # Get the vote count and calculate the percentage
        

        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
