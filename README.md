# 🎬 Movie Recommender Engine

This is a simple **content-based movie recommender system** built using Python. It suggests similar movies based on user input using **cosine similarity** on features such as genres, keywords, cast, and director.

## 🚀 Features

- Content-based filtering using movie metadata
- Combines features like genres, keywords, cast, and director
- Computes similarity between movies using **cosine similarity**
- Returns the top 50 most similar movies to a given movie

## 🧠 How It Works

1. Loads a movie dataset (`movie_dataset.csv`)
2. Preprocesses metadata features (fills in NaN values)
3. Combines selected features into a single string for each movie
4. Converts the combined features into a **count matrix**
5. Computes **cosine similarity** scores between all movies
6. Returns top recommendations based on a selected movie title

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn

## 📂 Dataset

The project uses a CSV file named `movie_dataset.csv` which must contain the following columns:
- `index`
- `title`
- `keywords`
- `cast`
- `genres`
- `director`

Make sure your CSV includes these fields to ensure the recommender system works properly.

