import os

def read_tab_delimited_file(file_name):
    """
    Reads a tab-delimited file into a dictionary.

    Args:
        file_name (str): The name of the file to read.

    Returns:
        dict: A dictionary where each key-value pair corresponds to a row in the file.
    """
    data = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Ignore empty lines
                    columns = line.split('\t')
                    if len(columns) == 2:  # Assuming each row has two columns
                        key, value = columns
                        data[key] = value
                    else:
                        print(f"Skipping line: {line}. Expected two columns.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    return data

# Example usage
if __name__ == "__main__":

    file_name = 'parabolaconstraints.txt'  # Replace with your file name
    data = read_tab_delimited_file(file_name)
    print(data)