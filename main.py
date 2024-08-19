from SearchEngine import SearchEngine
from DocumentStructure import Document
engine = SearchEngine()
engine.add_document(Document(1, "Document 1", "This is the first document."))
engine.add_document(Document(2, "Document 2", "This document is the second one."))
engine.add_document(Document(3, "Document 3", "Another document to search."))

results = engine.search("document second")
for doc in results:
    print(f"Document ID: {doc.doc_id}, Title: {doc.title}")
