from whoosh import qparser
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import open_dir

schema = Schema(path=ID(stored=True), content=TEXT)

index_dir = r'D:\index'

# Open the index
index = open_dir(index_dir)

# Define a QueryParser
qp = qparser.QueryParser('content', schema=schema)

# Search for files containing the word "hello"
q = qp.parse('hello')

# Perform the search
with index.searcher() as searcher:
    results = searcher.search(q)
    for result in results:
        print(result['path'])
        print(result)
