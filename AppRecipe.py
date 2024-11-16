import streamlit as st
from rank_bm25 import BM25Okapi
import pandas as pd

# Load your DataFrames
df_ayam = pd.read_pickle('processed/df_indoRecipesAyam.pkl')
df_telur = pd.read_pickle('processed/df_indoRecipesTelur.pkl')

# Combine the DataFrames
df_combined = pd.concat([df_ayam, df_telur], ignore_index=True)

# Tokenize the clean_instructions column
tokenized_corpus = [doc.split() for doc in df_combined['clean_instructions'].apply(lambda x: ' '.join([' '.join(step) for step in x]))]

# Initialize BM25
bm25 = BM25Okapi(tokenized_corpus)

# Streamlit app
st.title("Recipe Search")

query = st.text_input("Enter your search query:")
if query:
    tokenized_query = query.split()
    doc_scores = bm25.get_scores(tokenized_query)
    top_n = bm25.get_top_n(tokenized_query, df_combined.index, n=5)

    st.write("Top 5 recipes:")
    for idx in top_n:
        title = df_combined.loc[idx, 'Title']
        ingredients = df_combined.loc[idx, 'Ingredients']
        steps = df_combined.loc[idx, 'Steps']

        st.subheader(title)
        st.write("**Ingredients:**")
        ingredients_list = ingredients.split('--')
        for ingredient in ingredients_list:
            if ingredient.strip():
                st.write(f"- {ingredient.strip()}")

        
        st.write("**Steps:**")
        steps_list = steps.split('--')
        for step in steps_list:
            if step.strip():
                st.write(f"- {step.strip()}")
