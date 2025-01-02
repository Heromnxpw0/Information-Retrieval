import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

class Data:
    def __init__(self, path):
        nltk.download('stopwords')
        nltk.download('punkt_tab')
        nltk.download('wordnet')
        with open(path, "r") as file:
            self.data = json.load(file)
        self.topics = list(self.data.keys())
        self.subtopics = []
        self.original_documents = []
        self.documents = []
        self.links = []
        self.titles = []
        self.stopwords = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        for topic in self.topics:
            self.subtopics += list(self.data[topic].keys())
            for subtopic in self.data[topic]:
                self.original_documents.append(self.data[topic][subtopic]['content'])
                self.documents.append(self.process_doc(self.data[topic][subtopic]['content']))
                self.links.append(self.data[topic][subtopic]['link'])
                self.titles.append(self.data[topic][subtopic]['title'])
                
    def process_doc(self, doc):
        doc = doc.lower()
        tokens = word_tokenize(doc)
        tokens = [word for word in tokens if word not in string.punctuation]
        tokens = [word for word in tokens if word not in self.stopwords]
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens]
        return " ".join(tokens)
        
    def get_links(self, indecies):
        return [self.links[i] for i in indecies]
    
    def get_titles(self, indecies):
        return [self.titles[i] for i in indecies]
        
        
                
if __name__ == "__main__":
    # Testing
    Data("App/data.json")