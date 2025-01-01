import wikipedia
import json

topics = ["Artificial Intelligence", "Machine Learning", "Data Science", "Big Data", "Cloud Computing", "Bioinformatics", "Data mining", "Cybersecurity"]


# title, text, content, link to the article

data = {}

count = 0
for topic in topics:
    data[topic] = {}
    results = wikipedia.search(topic)
    for result in results:
        try:
            page = wikipedia.page(result)
            data[topic][result] = {}
            data[topic][result]['title'] = page.title
            data[topic][result]['content'] = page.content
            data[topic][result]['link'] = page.url
            count += 1
        except:
            print(f"{result} not found, try smth else")
        
        
print(f"Found {count} articles")
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
        