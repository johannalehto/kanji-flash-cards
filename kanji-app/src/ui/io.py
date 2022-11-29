class Io:
    def write(self, text):
        print(text)
        return

    def read(self, text=""):
        return input(text).lower()