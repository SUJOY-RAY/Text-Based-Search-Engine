from Indexing import InvertedIndex
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
