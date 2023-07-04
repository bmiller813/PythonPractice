class Text(str):
    def duplicate(self):
        return self + self
    

class TrackableList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)

list = TrackableList()
list.append("1")