import streamlit as st
from vectorSpaceModel import VectorSpaceModel
from data import Data
from queryProcess import process_query
from exactmatch import ExactMatch
import numpy as np

data = Data("App/data.json")
vectorModel = VectorSpaceModel(data)
exactmatch = ExactMatch(data)


def main():
    # Set up the page title
    st.title("Information Retrieval System")
    # Sidebar for model selection
    st.sidebar.title("Choose a Retrieval Model")
    model = st.sidebar.radio(
        "Select the information retrieval model:",
        ("Probabilistic Model", "Vector Space Model")
    )

    # Display the selected model
    st.sidebar.write(f"You selected: **{model}**")

    # Main search box
    st.write("Enter your query below to retrieve relevant articles.")
    query = st.text_input("Search Query", placeholder="Type your search here...")

    if st.button("Search"):
        if query:
            st.write(f"You searched for: **{query}**")
            
            if query.startswith('"') and query.endswith('"'):
                st.write("Looking for exact match...")
                results, time = exactmatch.search(query[1:-1])
                links = data.get_links(results)
                titles = data.get_titles(results)
                st.write(f"Search completed in {time:.4f} seconds.")
                for title, link in zip(titles, links):
                    st.write(title)
                    st.markdown(f'<iframe src="{link}" width="800" height="600"></iframe>', unsafe_allow_html=True)
            else:
                st.write(f"Retrieving articles using the **{model}**")
                processed_query, abrquery, misspell, abrv = process_query(query)
                if misspell:
                    st.write("Did you mean: ", processed_query)
                
                if model == "Vector Space Model":
                    results, time = vectorModel.search(processed_query)[:5]
                    if abrv:
                        st.write(f"Searching for abbreviation expanded query: {abrquery}")
                        results2, time2 = vectorModel.search(abrquery)[:5]
                        results = list(set(np.concatenate((results, results2))))
                        time = time + time2
                    links = data.get_links(results)
                    titles = data.get_titles(results)
                    st.write(f"Search completed in {time:.4f} seconds.")
                    for title, link in zip(titles, links):
                        st.write(title)
                        st.markdown(f'<iframe src="{link}" width="800" height="600"></iframe>', unsafe_allow_html=True)
                
        else:
            st.error("Please enter a search query.")


if __name__ == "__main__":
    main()