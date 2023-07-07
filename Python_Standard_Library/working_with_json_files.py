import json
from pathlib import Path
# JSON = JavaScript Object Notation

## Creating a JSON file
# movies = [
#     { "id": 1, "title": "Terminator", "year": 1989},
#     { "id": 2, "title": "KindergartenCop", "year": 1993}
# ]

# data = json.dumps(movies)
# Path("movies.json").write_text(data)

## Reading a JSON file
data = Path("movies.json").read_text()
movies = json.loads(data) # Parsing the string into an array of objects /  list of dictonaries
print(movies)
print(movies[0])
print(movies[1]["title"])