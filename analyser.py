# imports the counter library from collections so i can count the errors in the logs for later use
from collections import Counter

# i created the class logAnalyser for the purpose of analysing each log and returns the type of log in the .txt file
class logAnalyser:

    # the main constructor which runs when the oobject is created
    def __init__(self, logs):
        self.logs = logs

    # this function counts how many INFO, WARNING and ERROR logs there are and returns it
    def count_levels(self):
        levels = [log.level for log in self.logs]
        return Counter(levels)
    
    # this function only counts the amount of ERROR logs in the .txt file and outputs the whole error log
    def find_errors(self):
        # i used list comprehension to filter the logs to where the word "ERROR" occurs and instead of just returning the ERROR log type, it returns the whole error log
        return [log for log in self.logs if log.level == "ERROR"]