
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error
import numpy as np

# Load dataset
movies = pd.read_csv('movielens_movies.csv')
ratings = pd.read_csv('movielens_ratings.csv')

# Merge datasets for a complete view
data = pd.merge(ratings, movies, on='movieId')

# Pivot to get a matrix of users and their movie ratings
user_movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')

# Replace NaNs with 0 for similarity calculation
user_movie_matrix.fillna(0, inplace=True)

# Calculate similarity between users
user_similarity = cosine_similarity(user_movie_matrix)
np.fill_diagonal(user_similarity, 0)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

# Recommendation function
def recommend_movies(user_id, num_recommendations=5):
    """Recommend movies based on user's preferences."""
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index
    recommendations = {}
    
    for similar_user in similar_users:
        similar_user_ratings = user_movie_matrix.loc[similar_user]
        for movie, rating in similar_user_ratings[similar_user_ratings > 4].items():
            if movie not in user_movie_matrix.loc[user_id] or np.isnan(user_movie_matrix.loc[user_id, movie]):
                recommendations[movie] = recommendations.get(movie, 0) + rating
    
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [movie for movie, score in sorted_recommendations[:num_recommendations]]

# Example Usage
if __name__ == "__main__":
    user_id = int(input("Enter your User ID: "))
    print("Recommended movies:", recommend_movies(user_id))
