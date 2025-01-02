import time

class ExactMatch:
    def __init__(self, data):
        self.data = data
        
    def search(self, query):
        before = time.time()
        results = []
        for i, doc in enumerate(self.data.documents):
            if query in doc:
                results.append(i)
        after = time.time()
        return results, after - before