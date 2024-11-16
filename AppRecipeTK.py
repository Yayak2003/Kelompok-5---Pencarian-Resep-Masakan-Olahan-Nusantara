import tkinter as tk
from tkinter import ttk
from rank_bm25 import BM25Okapi
import pandas as pd

# Load your DataFrame
# Load each pickle file into a DataFrame
df_ayam = pd.read_pickle('processed/df_indoRecipesAyam.pkl')
df_telur = pd.read_pickle('processed/df_indoRecipesTelur.pkl')
# ...More dataset pkl files here

# Combine the DataFrames
df_combined = pd.concat([df_ayam, df_telur], ignore_index=True)
# ... Also add more DataFrame here

# Tokenize the clean_instructions column
tokenized_corpus = [doc.split() for doc in df_combined['clean_instructions'].apply(lambda x: ' '.join([' '.join(step) for step in x]))]

# Initialize BM25
bm25 = BM25Okapi(tokenized_corpus)

# Function to search recipes
def search_recipes():
    query = search_entry.get()
    tokenized_query = query.split()
    doc_scores = bm25.get_scores(tokenized_query)
    top_n = bm25.get_top_n(tokenized_query, df_combined.index, n=5)
    
    results_list.delete(0, tk.END)
    for idx in top_n:
        title = df_combined.loc[idx, 'Title']
        results_list.insert(tk.END, title)

# Function to display recipe details
def show_details(event):
    selected_idx = results_list.curselection()[0]
    selected_title = results_list.get(selected_idx)
    recipe_idx = df_combined[df_combined['Title'] == selected_title].index[0]
    
    ingredients = df_combined.loc[recipe_idx, 'Ingredients']
    steps = df_combined.loc[recipe_idx, 'Steps']
    
    ingredients_text.delete(1.0, tk.END)
    ingredients_text.insert(tk.END, ingredients)
    
    steps_text.delete(1.0, tk.END)
    steps_text.insert(tk.END, steps)

# Create the main window
root = tk.Tk()
root.title("Recipe Search")

# Create and place the search entry
search_entry = ttk.Entry(root, width=50)
search_entry.pack(pady=10)

# Create and place the search button
search_button = ttk.Button(root, text="Search", command=search_recipes)
search_button.pack(pady=5)

# Create and place the results listbox
results_list = tk.Listbox(root, width=50, height=10)
results_list.pack(pady=10)
results_list.bind('<<ListboxSelect>>', show_details)

# Create and place the ingredients text box
ingredients_label = ttk.Label(root, text="Ingredients:")
ingredients_label.pack(pady=5)
ingredients_text = tk.Text(root, width=50, height=10)
ingredients_text.pack(pady=5)

# Create and place the steps text box
steps_label = ttk.Label(root, text="Steps:")
steps_label.pack(pady=5)
steps_text = tk.Text(root, width=50, height=10)
steps_text.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
