import sqlite3

conn = sqlite3.connect('SJreader.db')
conn.execute('DROP TABLE recent_articles;')
conn.execute('''CREATE TABLE recent_articles(
id INTEGER PRIMARY KEY,
title text,
abstract text,
journal text,
author1 text,
author2 text,
author3 text,
author4 text,
author5 text,
author6 text,
doi text,
url text,
keyword1 text,
keyword2 text,
keyword3 text,
keyword4 text,
pubdate text,
OA text);''')

conn.close()