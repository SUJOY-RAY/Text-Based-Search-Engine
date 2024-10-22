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

    search_engine.add_document(Document(1, "Doc 1", "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"))

    search_engine.add_document(Document(2, "Doc 2", "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?"))

    search_engine.add_document(Document(3, "Doc 3", "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat."))

    query = "consequatur"

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
