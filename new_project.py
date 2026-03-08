import re
file = open("logs.txt", "r")
for line in file:
    print(line)
file.close()

pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (INFO|ERROR|WARNING) (.*)"

with open("logs.txt") as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            date = match.group(1)
            time = match.group(2)
            log = match.group(3)
            message = match.group(4)

            print(date, time, log, message)
