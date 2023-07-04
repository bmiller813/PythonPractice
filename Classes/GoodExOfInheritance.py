class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened = False
   
    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream been open buddy")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream been closed buddy")
        self.opened = False
   
class FileStream(Stream):
    def read(self):
        print("Reading yo file data buddy")

class NetworkStream(Stream):
    def read(self):
        print("Reading yo network data buddy")