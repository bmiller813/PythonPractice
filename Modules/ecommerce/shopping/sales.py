# from ecommerce.customer import contact # Absolute Import (Intra Package References) -> BEST PRACTICE
# from ..customer import contact # Relative Import


#print("Sales Inatialized - ", __name__)

def calc_tax():
    pass


def calc_shipping():
    pass

# Scripts
if __name__ == "__main__": 
    print("Sales Started")
    calc_tax()