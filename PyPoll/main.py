# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
election_csv = os.path.join("Resources", "election_data.csv")       # Input file path
analysis_path = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0                                                     # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_list = []                                                 #list for candidate names
candidate_votes = {}                                                #dictionary to store votes for each candidate

# Winning Candidate and Winning Count Tracker
winning_candidate = ""                                               #storing winning names in a list
winning_count = 0                                                    #storing an integer in a list

# Open the CSV file and process it
with open(election_csv) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="\n")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2] 

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)                       #add name to the list
            candidate_votes[candidate_name] = 0                         #adds name to the dictionary and initialize their vote count to 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1                            #increment the candidate's vote by 1 in the dictionary

# Open a text file to save the output
with open(analysis_path, "w") as txt_file:

    # Print the total vote count (to terminal)
    election_results = (f"Election Results\n"
                        f"--------------------------\n"
                        f"Total Votes: {total_votes}\n"
                        f"--------------------------\n")
    print(election_results)

    # Write the total vote count to the text file
    txt_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name in candidate_list:
        
        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = (votes/total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate_name

        # Print and save each candidate's vote count and percentage
        vote_summary = (f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n")
        print(vote_summary)
        txt_file.write(vote_summary)

    # Generate and print the winning candidate summary
    winner = (f"-------------------------\n"
                      f"Winner: {winning_candidate}\n"
                      f"-------------------------\n")
    print(winner)
    # Save the winning candidate summary to the text file
    txt_file.write(winner)