import re
from log_entry import Entry

file = open("logs.txt", "r")
for line in file:
    print(line)
file.close()

pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (INFO|ERROR|WARNING) (.*)"

def parse_logs():
    logs = []
    with open("logs.txt") as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                entry = Entry(
                    match.group(1),
                    match.group(2),
                    match.group(3),
                    match.group(4))
                
                logs.append(entry)
    return logs