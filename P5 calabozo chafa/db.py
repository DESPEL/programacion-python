import pickle
from collections import namedtuple


class DB:
    def __init__(self, filename):
        self.filename = filename
        self.__create_file_if_not()

        self.load_data()

    def append(self, data):
        self.data.append(data)
        self.update()

    def load_data(self):
        with open(self.filename, 'rb') as f:
            val = f.read()
            if len(val) == 0:
                self.data = [{}, ]
                return
            self.data = pickle.loads(val)
            if type(self.data) is not list:
                self.data = [self.data, ]

    def update(self):
        with open(self.filename, 'wb') as f:
            datastring = pickle.dumps(self.data)
            f.write(datastring)

    def save(self): self.update()

    def __create_file_if_not(self):
        with open(self.filename, 'a') as f:
            pass


if __name__ == "__main__":
    test = DB("test.csv")
    print(test.data[0])
    test.data[0] = "abcdefghij"
    test.data.append("jasdfkasdfas")
    test.save()
    print(test.data)