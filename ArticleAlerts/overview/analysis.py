import matplotlib.pyplot as plt

class Analyser:

    def __init__(self, data=[], yes_no=True):
        self.data = data
        if yes_no:
            self.yes = 0
            self.no = 0

    def analyse(self, data, topics):
        self.add_data(data)
        self.check_topic(topics)
        self.clear_data()

    def check_topic(self, topic):
        for data in self.data:
            search = [item.lower() in data for item in topic]
            if any(search):
                self.yes = self.yes +1
            else:
                self.no= self.no +1

    def add_data(self, new_data):
        self.data = self.data + new_data

    def clear_data(self):
        self.data = []

    def plot(self):
        plt.bar(["Yes", "None"], [self.yes, self.no])
        plt.show()
