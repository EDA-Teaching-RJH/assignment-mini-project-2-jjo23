# imported the regular expressions from the library
import re
# i imported the Entry class from the log_entry file so i can store information about each log line
from log_entry import Entry


file = open("logs.txt", "r")
for line in file:
    print(line)
file.close()

# this pattern is the base pattern of the text which is used to compare with the logs.txt file
pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (INFO|ERROR|WARNING) (.*)"

# this function takes one input and then reads the file, and then returns the logs
def parse_logs():
    # empty list that will be used to store entries
    logs = []
    # this opens the file log
    with open("logs.txt") as file:
        for line in file:
            # this checks the line and compares it to the pattern and then stores that in a variable 
            match = re.search(pattern, line)
            if match:
                # if there's a match, the log will then get extracted and each variable will be put into their respective groups (date, time, level and message)
                entry = Entry(
                    match.group(1),
                    match.group(2),
                    match.group(3),
                    match.group(4))
                # this just stores the entry to a list
                logs.append(entry)
    return logs