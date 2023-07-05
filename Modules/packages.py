# This import is red due to moving the sales.py into a different directory
# Add a file called __init__.py into the ecommerce directory to treat it as a package
# Packagae = Container to 1 or more modules
#import sales
from ecommerce.sales import calc_tax, calc_shipping

from ecommerce import sales

calc_tax()
sales.calc_shipping()