class Entry:

    def __init__(self, date, time, log, message):
        self.date = date
        self.time = time
        self.log = log
        self.message = message

    def __str__(self):
        return f"{self.date} {self.time} {self.log} {self.message}"

