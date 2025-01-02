import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data import Data
import time

class VectorSpaceModel:
    def __init__(self, data):
        self.data = data
        self.vectorizer = TfidfVectorizer()
        self.vectorizer.fit(self.data.documents)    
        self.vector_space = self.vectorizer.transform(self.data.documents)
        
    def search(self, query):
        before = time.time()
        query = self.data.process_doc(query)
        query_vector = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vector, self.vector_space).flatten()
        most_similar = np.argsort(cosine_similarities)[::-1]
        after = time.time()
        return most_similar, after - before


if __name__ == "__main__":
    # Testing
    data = Data("App/data.json")
    model = VectorSpaceModel(data)
    results = model.search("Cyber")[:5]
    links = model.data.get_links(results)
    print(links)