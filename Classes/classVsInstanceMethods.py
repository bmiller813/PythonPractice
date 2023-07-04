class Point:
    def __init__(self, x, y): # Magic Method
        self.x = x
        self.y = y

    @classmethod # Decorator 
    def zero(cls): # cls by convention when defining class method
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")



point = Point.zero()
point.draw()