import streamlit as st
from rank_bm25 import BM25Okapi
import pandas as pd

# Load your DataFrames
df_ayam = pd.read_pickle('processed/df_indoRecipesAyam.pkl')
df_ikan = pd.read_pickle('processed/df_indoRecipesIkan.pkl')
df_kambing = pd.read_pickle('processed/df_indoRecipesKambing.pkl')
df_sapi = pd.read_pickle('processed/df_indoRecipesSapi.pkl')
df_tahu = pd.read_pickle('processed/df_indoRecipesTahu.pkl')
df_tempe = pd.read_pickle('processed/df_indoRecipesTempe.pkl')
df_telur = pd.read_pickle('processed/df_indoRecipesTelur.pkl')
df_udang = pd.read_pickle('processed/df_indoRecipesUdang.pkl')


# Combine the DataFrames
df_combined = pd.concat([df_ayam, df_ikan, df_kambing, df_sapi, df_tahu, df_tempe, df_telur, df_udang], ignore_index=True)

# Tokenize the clean_instructions column
tokenized_corpus = [doc.split() for doc in df_combined['clean_instructions'].apply(lambda x: ' '.join([' '.join(step) for step in x]))]

# Initialize BM25
bm25 = BM25Okapi(tokenized_corpus)

# Streamlit app
st.markdown("<h1 style='text-align: center; color: #FF6347;'>🍽️ Resep Makanan Nusantara 🍽️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Temukan resep terbaik berdasarkan bahan yang kamu inginkan!</p>", unsafe_allow_html=True)

# User enters a query
query = st.text_input("🔍 Masukkan kata kunci pencarian resep (contoh: ayam, ikan, telur,sapi, kambing dll.):")
st.markdown("---")

if query:
    tokenized_query = query.split()
    doc_scores = bm25.get_scores(tokenized_query)
    top_n = bm25.get_top_n(tokenized_query, df_combined.index, n=7)

    # Show top 5 recipes as buttons
    st.markdown("<h3 style='color: #FF4500;'> Top 7 Rekomendasi:</h3>", unsafe_allow_html=True)
    recipe_titles = df_combined.loc[top_n, 'Title'].tolist()
    
    # Create a button for each recipe
    for idx, title in zip(top_n, recipe_titles):
        if st.button(title, key=idx):  # Using the title as button label
            ingredients = df_combined.loc[idx, 'Ingredients']
            steps = df_combined.loc[idx, 'Steps']
            
            # Display ingredients
            st.markdown("<h3 style='color: #4682B4;'>📝 Bahan-Bahan:</h3>", unsafe_allow_html=True)
            ingredients_list = ingredients.split('--')
            st.markdown("<ul>", unsafe_allow_html=True)
            for ingredient in ingredients_list:
                if ingredient.strip():
                    st.markdown(f"<li style='font-size: 16px;'>{ingredient.strip()}</li>", unsafe_allow_html=True)
            st.markdown("</ul>", unsafe_allow_html=True)

            # Display steps
            st.markdown("<h3 style='color: #4682B4;'>🍳 Langkah-Langkah:</h3>", unsafe_allow_html=True)
            steps_list = steps.split('--')
            for i, step in enumerate(steps_list):
                if step.strip():
                    st.markdown(f"<p><strong>Langkah {i + 1}:</strong> {step.strip()}</p>", unsafe_allow_html=True)

            # Add a separation line
            st.markdown("---")

# Footer
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ by Kelompok 5</p>", unsafe_allow_html=True)
