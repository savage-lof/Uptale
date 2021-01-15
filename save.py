import sqlite3

con = sqlite3.connect("uptale.db")
cur = con.cursor()
result = cur.execute("""SELECT * FROM save ORDER BY ID DESC LIMIT 1""").fetchone()
first_result = cur.execute('''SELECT * FROM save''').fetchone()
