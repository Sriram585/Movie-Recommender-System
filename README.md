# Movie Recommender System

A simple and efficient **movie recommender system** that uses **cosine similarity** to suggest similar movies based on user input.

## Project Overview

This project recommends movies that are similar to a movie selected by the user. It leverages content-based filtering using metadata such as genres, keywords, cast, and crew to compute similarity between movies.

## Features

- Recommend similar movies based on selected movie title
- Uses cosine similarity for content-based filtering
- Clean and interactive interface (optional: via Streamlit)
- Built with Python and Scikit-learn

## How It Works

1. **Data Preprocessing:** Load and clean the dataset (e.g., TMDB 5000 movie dataset).
2. **Feature Extraction:** Combine features like genres, keywords, overview, cast, and crew into a single string.
3. **Vectorization:** Use `CountVectorizer` to convert text into vectors.
4. **Similarity Computation:** Use **cosine similarity** to find similar movies.
5. **Recommendation:** Return top 5 or 10 similar movies based on the cosine similarity score.

## 🛠️ Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn (CountVectorizer, cosine_similarity)
- Streamlit
