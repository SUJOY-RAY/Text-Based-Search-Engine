class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add_document(self, doc):
        terms = doc.content.lower().split()  # Tokenize content
        for term in terms:
            if term not in self.index:
                self.index[term] = set()
            self.index[term].add(doc.doc_id)
