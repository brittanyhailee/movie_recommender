import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    return df[df.title.str.lower() == title.lower()]["index"].values[0]
  

# read CSV file:
df = pd.read_csv('movie_dataset.csv')

# features to look for similarity: genres, keywords
features = ['keywords', 'cast', 'genres', 'director']
 
# create a column in DF to combine all selected features
# get rid of all NaN from the selected features
for feature in features:
    df[feature] = df[feature].fillna('')

def combine_features(row):
    try:
        return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']
    except:
        print("Error", row)


df['combined_features'] = df.apply(combine_features, axis=1)
# print("\nCombined Features: ")
# print(df['combined_features'].head())

# create count matrix from the new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(df['combined_features'])

# compute the cosine similarity based on the count matrix
similarity_scores = cosine_similarity(count_matrix)

user_likes = "Tangled"

# get index of this movie from its title
# index = df[df['title'].str.lower() == user_likes.lower()].index.values
# print(index)
movie_index = get_index_from_title(user_likes)
similar_movies = list(enumerate(similarity_scores[movie_index]))

# get a list of similar movies in descending order of similarity score
# we do x[1] because our similar_movies array is: [movie_index, similarity_score]
sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True) # reverse=True to sort in descending order

# print titles of first 50 movies
print("Since user liked \"" + user_likes  + "\": ")
i = 1
for movie in sorted_similar_movies[1:]:
    # movie = [movie_index, similarity_score]
    print(get_title_from_index(movie[0]))
    i += 1
    if i > 50: 
        break