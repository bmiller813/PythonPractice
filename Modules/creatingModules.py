# Moved the class to sales.py (similar classes get grouped together)
# Bad practice to import all using *import sales
from sales import calc_shipping, calc_tax
import sales #Another way to import methods

sales.calc_shipping() # Line

calc_shipping()
calc_tax()



