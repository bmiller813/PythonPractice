from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass


class Stream(ABC):
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

    @abstractmethod
    def read(self):
        pass
   
class FileStream(Stream):
    def read(self):
        print("Reading yo file data buddy")

class NetworkStream(Stream):
    def read(self):
        print("Reading yo network data buddy")

class MemoryStream(Stream):
    def read(self):
        print("Reading yo memory stream data buddy")

stream = MemoryStream()
stream.open()