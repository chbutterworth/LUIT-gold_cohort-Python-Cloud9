import os
from datetime import datetime

# Get the current working directory
current_directory = os.getcwd()

# Initialize an empty list to store file information
file_list = []

# Iterate through the files in the current directory
for filename in os.listdir(current_directory):
    # Check if the item is a file (not a directory)
    if os.path.isfile(filename):
        # Get file size and last modification time
        file_size = os.path.getsize(filename)
        modification_time_timestamp = os.path.getmtime(filename)

        # Convert the modification time to a human-readable format
        modification_time = datetime.fromtimestamp(modification_time_timestamp)

        # Create a dictionary with file information
        file_info = {
            'filename': filename,
            'size_bytes': file_size,
            'modification_time': modification_time.strftime('%Y-%m-%d %H:%M:%S')
        }

        # Append the dictionary to the file_list
        file_list.append(file_info)

# Print the list of dictionaries
for file_info in file_list:
    print(file_info)