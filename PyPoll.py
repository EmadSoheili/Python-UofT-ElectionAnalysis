
# PyPoll with Python Project
# University of Toronto - Data Analytics Boot Camp - Module 1 - PyPoll with Python

# Import Modules ================================================================================
import csv
import os

# Set file paths ================================================================================

    # Assign input and output file paths to variables 
file_to_load = "/Users/emadsoheili/DA/GitHub/Python-UofT-ElectionAnalysis/Resources/election_results.csv"
file_to_save = "/Users/emadsoheili/DA/GitHub/Python-UofT-ElectionAnalysis/Analysis/election_analysis.txt"

# Initialize some variables ================================================================================

        # Add a accumulator and set it to zero
total_votes = 0

        # Create an empty list for candidates' names
candidate_options = []

# Read the data ================================================================================

    # Open the election file 
with open(file_to_load) as election_data:

    # Read file 
    file_reader = csv.reader(election_data)

    # Read headers 
    headers = next(file_reader)

# Analyze the data ================================================================================

    # Go through every single rows
    for row in file_reader:

    # Count total votes
        total_votes += 1

# Print the analysis output ================================================================================

print(total_votes)



