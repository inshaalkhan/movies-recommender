# Movie Recommendation System

## Link - https://movies-recommender-by-inshaal.streamlit.app/

## Project Overview

The **Movie Recommendation System** is a machine learning project that recommends movies similar to a given movie title. The system analyzes movie content such as **genres, keywords, cast, and overview** to find similarities between movies and generate recommendations.

This project implements a **Content-Based Recommendation System** using Natural Language Processing (NLP) techniques and similarity measures to suggest movies that are most similar to the selected one.

For example, if a user searches for **"Avatar"**, the system will recommend movies with similar themes, genres, and cast.

---

# Features

* Recommends **Top 5 similar movies**
* Uses **content similarity between movies**
* Efficient similarity computation using **Cosine Similarity**
* Machine learning preprocessing for text features
* Model persistence using **Pickle**
* Easy integration with a **web application interface**

---

# Machine Learning Algorithm Used

### Content-Based Filtering

The recommendation system uses **Content-Based Filtering**, which suggests movies based on the similarity of movie attributes.

Instead of relying on user ratings, the system compares movie features such as:

* Genre
* Cast
* Keywords
* Overview
* Director

Movies with similar features are recommended to the user.

---

#  Techniques Used

### 1. Feature Engineering

Multiple movie attributes were combined to create a **single text feature called `tags`**.
This helps the model understand the overall context of a movie.

Combined features include:

* Genres
* Keywords
* Cast
* Director
* Overview

Example:

Action Adventure Sci-Fi James Cameron Space Alien

---

### 2. Text Vectorization

The textual movie features are converted into **numerical vectors** so that machine learning algorithms can process them.

Technique used:

**Count Vectorization**

It converts text into a matrix of token counts.

Example:

Movie Text → Vector Representation

```
Action Adventure Space
```

becomes

```
[1, 1, 0, 1, 0]
```

---

### 3. Similarity Measurement

To measure how similar two movies are, the system uses:

**Cosine Similarity**

Cosine similarity calculates the cosine of the angle between two vectors.

Similarity Score Range:

* **1 → Highly Similar**
* **0 → No Similarity**

This allows the system to identify movies that are most similar in terms of content.

---

#  Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* NLTK
* Pickle

### Machine Learning Tools

* CountVectorizer
* Cosine Similarity

---

#  Development Environment

The project was developed using:

* **Python**
* **Jupyter Notebook / Google Colab**
* **Pandas & NumPy for data processing**
* **Scikit-learn for machine learning**
* **NLTK for text processing**

Development tools:

* Google Colab
* Jupyter Notebook
* Git & GitHub

---

#  Deployment Environment

The trained recommendation model can be deployed using:

* **Streamlit** (for building a web interface)
* **Python backend**
* Model files stored using **Pickle (.pkl)**

Deployment workflow:

1. Train model in Jupyter/Colab
2. Save similarity matrix and movie data using Pickle
3. Load the model in a Streamlit application
4. User selects a movie
5. System displays recommended movies

---

#  Project Structure

```
Movie-Recommendation-System

│
├── Movie_Recommendation_System.ipynb
├── movies.pkl
├── similarity.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

#  Project Workflow

1. Load movie datasets
2. Data preprocessing and cleaning
3. Feature extraction
4. Combine important columns into tags
5. Text vectorization using CountVectorizer
6. Compute similarity using Cosine Similarity
7. Generate recommendations
8. Save model using Pickle
9. Deploy using Streamlit

---

#  Dataset

The dataset contains information about movies such as:

* Title
* Genres
* Cast
* Keywords
* Overview
* Director

The dataset is processed to extract meaningful features used for similarity comparison.

---

#  Example Output

Input:

```
Avatar
```

Output:

Recommended Movies

* Guardians of the Galaxy
* John Carter
* Star Trek
* Interstellar
* The Avengers






