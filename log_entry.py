# this file represents one log entry

# i created the Entry class to act as a blueprint for creating objects within the logs.txt file
class Entry:

    # the constructor within the entry class which runs automatically when a new object is created
    def __init__(self, date, time, level, message):
        # assigns the parameters to their respective variables to store specific information
        self.date = date
        self.time = time
        self.level = level
        self.message = message

    # this function only controls how the object will be outputted when called (basically acts as a print() function)
    def __str__(self):
        return f"{self.date} {self.time} {self.level} {self.message}"

