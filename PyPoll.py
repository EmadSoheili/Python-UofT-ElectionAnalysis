
# PyPoll with Python Project
# University of Toronto - Data Analytics Boot Camp - Module 1 - PyPoll with Python

# Import Modules ================================================================================
import csv

# Set file paths ================================================================================

# Assign input and output file paths to variables 
file_to_load = "/Users/emadsoheili/DA/GitHub/Python-UofT-ElectionAnalysis/Resources/election_results.csv"
file_to_save = "/Users/emadsoheili/DA/GitHub/Python-UofT-ElectionAnalysis/Analysis/election_analysis.txt"

# Initialize some variables ================================================================================

# Add a accumulator and set it to zero
total_votes = 0

# Create an empty list for candidates' names
candidate_options = []

# Create an empty dictionary for the candidates' votess
candidate_votes = {}

# Declare variables about the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read the data ================================================================================

# Open the election file 
with open(file_to_load) as election_data:

    # Read file 
    file_reader = csv.reader(election_data)

    # Read headers 
    headers = next(file_reader)

# Calculate each candidates' votes ================================================================================

    # Go through every single rows
    for row in file_reader:

        # Count total votes
        total_votes += 1

        # Extract candidate's name using indexing
        candidate_name = row[2]

        # Add unique candidate's name to the list
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            # Add keys and values to candidate_votes dictionary
            candidate_votes[candidate_name] = 0

        # Count each candidates' votess
        candidate_votes[candidate_name] += 1

# Print the analysis output in terminal ================================================================================

print(
    f"\nElection Results\n"
    f"-----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-----------------------------")

for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes) * 100

    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes})')

    if votes > winning_count:
        
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

print(
    f"-----------------------------\n"
    f"Winnier: {winning_candidate}\n"
    f"Winner's Votes: {winning_count}\n"
    f"Winner's Percentage {winning_percentage:.1f}%\n"
    f"-----------------------------")

# Print the analysis output in txt file ================================================================================

with open(file_to_save,"w") as txt_file:

    txt_file.write(
        f"\nElection Results\n"
        f"-----------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------------------\n")

    for candidate_name in candidate_votes:
        
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        txt_file.write(f'{candidate_name}: {vote_percentage:.1f}% ({votes})\n')

    txt_file.write(
    f"-----------------------------\n"
    f"Winnier: {winning_candidate}\n"
    f"Winner's Votes: {winning_count}\n"
    f"Winner's Percentage {winning_percentage:.1f}%\n"
    f"-----------------------------")
