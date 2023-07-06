from pathlib import Path

# # Windows
# Path("C:\\Program Files\\Microsoft") # Absolute Path
# Path(r"C:\Program Files\Microsoft") # Raw String

# # Mac \ Linux
# Path("/usr/local/bin")

# Path()
# Path("ecommerce/__init__.py") # Relative
# Path() / "ecommerce" / "__init__.py"
# Path.home()

path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
# path = path.with_name("file.txt")
path = path.with_suffix(".txt")
print(path)
