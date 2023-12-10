import sys
import numpy as np
import pandas as pd

    # Additional checks can be added here if needed
def print_help():
    print("Apriori.py usage:")
    print("python Apriori.py path/to/data sup% [conf%]")
    print("Computes the biggest and most frequent itemset of the dataset")


def validate_arguments(path, float1, float2):
    # Check if floats are less than one
    if not (0 <= float1 <= 1) or not (0 <= float2 <= 1):
        print_help()
        sys.exit(1)

def read_params():
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print_help()
        sys.exit(1)

    optional_param = 1.0

    # Get arguments
    path = sys.argv[1]
    float1 = float(sys.argv[2])

    # Check if the optional parameter is provided
    if len(sys.argv) == 4:
        optional_param = float(sys.argv[3])

 
    # Validate arguments
    validate_arguments(path, float1, optional_param)
    return path, float1, optional_param

def load_data(file_path):
	with open(file_path, 'r') as file:
		lines = file.readlines()

	return [row.strip().split(';') for row in lines]

def count_unique_values(data):
    """
    Count occurrences of unique values in a list of lists.

    Args:
    - data (list): List of lists containing elements.

    Returns:
    - dict: Dictionary with unique values as keys and their counts as values.
    """
    unique_counts = {}
    for row in data:
        for element in row:
            if element != '':
                unique_counts[element] = unique_counts.get(element, 0) + 1
    return unique_counts

def apriori(data, minsup, minconf):
	# Find unique values
	C1 = count_unique_values(data)
	print("Scan T -> C1: ", [f'{value}: {count}' for value, count in C1.items()])
	#

if __name__ == "__main__":
	data_path, minsup, minconf = read_params()
	data = load_data(data_path)
	data = [[element for element in row if element != ''] for row in data]

