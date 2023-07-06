from pathlib import Path

path = Path("Modules")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# for p in path.iterdir():
#     print(p)

# If you don't have a bunch of files,
# we can convert this generator to a list using a list comprehension
# Can't search by pattern or recusrivly -> use glob for this
path = [p for p in path.iterdir() if p.is_dir()]
# py_files = [p for p in path.glob("*.py")]
py_files = [p for p in path.rglob("*.py")] # Recursive
print(py_files)
