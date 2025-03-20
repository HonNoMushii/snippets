import sys
import os
import json
import argparse

# Get the arguments from the command line
print(sys.argv)
# length of total arguments
print(len(sys.argv))
print(os.path)

filename = sys.argv[1]
if filename.endswith(".txt"):
    filename = filename[:-4]
elif filename.endswith(".csv"):
    filename = filename[:-4]
elif filename.endswith(".json"):
    filename = filename[:-5]
else:
    filename = filename
    raise ValueError(f"File extension of {filename} is not supported.")
    
    
    
    
quary= sys.argv[2]

with open(filename, "w+") as file:
    file.write(quary)