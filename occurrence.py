class occurrence:

    def __init__(self, filename, word):
        self.records = {filename: (filename, 1)}
        self.word = word

    def __str__(self):
        result = ""
        for key in self.records:
            result += self.records[key].__str__()
        return result

    def update(self, word, filename):
        if self.records.get(filename) is not None:
            currentrecord = self.records[filename]
            self.records[filename] = (filename, currentrecord[1]+1)
        elif self.records.get(filename) is None:
            self.records[filename] = (filename, 1)
