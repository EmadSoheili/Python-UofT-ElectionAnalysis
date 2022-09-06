
# PyPoll with Python Project
# University of Toronto - Data Analytics Boot Camp - Module 1 - PyPoll with Python

# Read the data ================================================================================
import csv
import os

    # Assign input and output file paths to variables ---------------
file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("Analysis","electionAnalysis.txt")

    # Open the election file ---------------
with open(file_to_load) as election_data:

    # Read file ---------------
    file_reader = csv.reader(election_data)

    # Read headers ---------------
    headers = next(file_reader)
    print(headers)



