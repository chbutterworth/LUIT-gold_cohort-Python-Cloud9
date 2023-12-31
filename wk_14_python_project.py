#!/usr/bin/env python3.8.16

import os

# Get the current working directory
current_dir = os.getcwd()

# Create an empty list to store file info
file_info = []

# Go through the directory tree and get file info
for dirpath, dirnames, filenames in os.walk(current_dir):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        file_size = os.path.getsize(file_path)
        file_info.append({"name": file, "size": file_size})

# Print the list of file information
for file in file_info:
    print(file)
