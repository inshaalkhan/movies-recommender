import streamlit as st
import pickle
import pandas as pd
import requests
import base64



def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("background.JPG")


# -----------------------------
# Fetch movie poster from TMDB
# -----------------------------
def fetch_poster(movie_id):

    api_key = "29109fdd0a93d5040f2642434c78d6fe"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    try:

        data = requests.get(url)
        data = data.json()

        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"

    except:
        return "https://via.placeholder.com/500x750?text=Error"


# -----------------------------
# Recommendation Function
# -----------------------------
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)

        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# -----------------------------
# Load Data
# -----------------------------
movies = pickle.load(open('movies.pkl', 'rb'))

similarity = pickle.load(open('similarity.pkl', 'rb'))
#-----------------------------------------

st.markdown("""
<style>



/* Button Style */

div.stButton > button {
    background: linear-gradient(90deg,#ff4b2b,#ff416c);
    color:white;
    border-radius:10px;
    font-size:18px;
    padding:10px 30px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Streamlit UI
# -----------------------------
st.markdown("""
<h1 style='text-align:center;
font-size:70px;
font-weight:550;
color:white;
margin-top:-20px;
letter-spacing:2px;'>
Movie Recommender
</h1>
""", unsafe_allow_html=True)

st.markdown(
"<h3 style='text-align:center; color:white; margin-top:-10px; margin-bottom:0px;'>Discover your next favorite movie, tailored to your taste</h3>",
unsafe_allow_html=True
)

selected_movie_name = st.selectbox(
    " ",
    movies['title'].values
)


# -----------------------------
# Recommend Button
# -----------------------------
if st.button("Recommend"):

    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.write(names[0])

    with col2:
        st.image(posters[1])
        st.write(names[1])

    with col3:
        st.image(posters[2])
        st.write(names[2])

    with col4:
        st.image(posters[3])
        st.write(names[3])

    with col5:
        st.image(posters[4])
        st.write(names[4])