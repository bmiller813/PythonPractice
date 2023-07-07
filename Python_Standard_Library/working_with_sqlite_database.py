import sqlite3
import json
from pathlib import Path
# SQLite = Lightweight Database used for storing app data
# Often used for small apps like the ones ran on phones and tablets

## Writing to a DB
#movies = json.loads(Path("movies.json").read_text())

# Will create if this doesn't exist
# The connection object would have to be closed when done so instead ->
# <- we should use with statement
# We have to create a command (Instruction sent to db)
# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

## Reading a DB
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)