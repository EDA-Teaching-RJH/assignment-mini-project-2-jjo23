class Entry:

    def __init__(self, date, time, level, message):
        self.date = date
        self.time = time
        self.level = level
        self.message = message

    def __str__(self):
        return f"{self.date} {self.time} {self.level} {self.message}"

