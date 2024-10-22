import time

class Document:
    def __init__(self, doc_id, title, content):
        self.doc_id = doc_id
        self.title = title
        self.content = content

class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add_document(self, doc):
        terms = doc.content.lower().split()  # Tokenize content
        for term in terms:
            if term not in self.index:
                self.index[term] = set()
            self.index[term].add(doc.doc_id)

class SearchEngine:
    def __init__(self):
        self.index = InvertedIndex()
        self.documents = {}

    def add_document(self, doc):
        self.documents[doc.doc_id] = doc
        self.index.add_document(doc)

    def search(self, query):
        query_terms = query.lower().split()
        if not query_terms:
            return []

        result_set = None
        for term in query_terms:
            if term in self.index.index:
                if result_set is None:
                    result_set = self.index.index[term].copy()
                else:
                    result_set &= self.index.index[term]
            else:
                result_set = set()

        return [self.documents[doc_id] for doc_id in result_set] if result_set else []

def normal_search(documents, query):
    query_terms = query.lower().split()
    results = []
    for doc in documents.values():
        if all(term in doc.content.lower() for term in query_terms):
            results.append(doc)
    return results

if __name__ == "__main__":
    search_engine = SearchEngine()

    search_engine.add_document(Document(1, "Doc 1", "This is a sample document."))
    search_engine.add_document(Document(2, "Doc 2", "This document is another example."))
    search_engine.add_document(Document(3, "Doc 3", "Sample documents are great for testing."))

    query = "sample document"

    start_time_normal = time.time()
    normal_results = normal_search(search_engine.documents, query)
    end_time_normal = time.time()
    normal_search_time = end_time_normal - start_time_normal

    start_time_engine = time.time()
    engine_results = search_engine.search(query)
    end_time_engine = time.time()
    engine_search_time = end_time_engine - start_time_engine

    print("Normal Search Results:")
    for doc in normal_results:
        print(f"- {doc.title}")

    print(f"Normal Search Time: {normal_search_time:.6f} seconds")

    print("\nSearch Engine Results:")
    for doc in engine_results:
        print(f"- {doc.title}")

    print(f"Search Engine Time: {engine_search_time:.6f} seconds")
