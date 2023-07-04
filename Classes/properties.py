class Product:
    def __init__(self, price):
        self.price = price

    @property   # We can do this instead of explicitly calling ln 14
    def price(self):
        return self.__price

    @price.setter # Same as ln 5 comment
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative...")
        self.__price = value

    # price = property(get_price, set_price)


product = Product(10)
product.price = 2
print(product.price)
