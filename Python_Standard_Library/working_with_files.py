from pathlib import Path
from time import ctime
import shutil


# path = Path("modules/ecommerce/__init__.py")
source = Path("modules/ecommerce/__init__.py")
target = Path() / "__init__.py"
# path.exists()
# path.rename("init.txt")
# path.unlink() # Delete
# print(ctime(path.stat().st_ctime)) 

# with open("__init__.py", "r") as file:
#     ...

# path.read_bytes()
# path.read_text() # This method is easier than the built in open function (line 10)
# path.write_text()
# path.write_bytes()

# When it comes to copying a file, this path object is not the ideal way
# This is a little tedius and there is a better way
target.write_text(source.read_text())

# The better way:
shutil.copy(source, target) # Easier and cleaner