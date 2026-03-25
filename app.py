import streamlit as st
import pickle
import requests
import os
import gdown
import pandas as pd


st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

API_KEY = st.secrets.get("TMDB_API_KEY", "")

PLACEHOLDER_POSTER = "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba"

MOVIES_FILE_ID = "12Hmtq0p_ve2dpDeNhauIIQdIiOhf6ITm"
SIMILARITY_FILE_ID = "1wFFhiwwzKmBN_IygPmWwvNpY99pWR0LR"


def download_file(file_id, output):
    if not os.path.exists(output):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output, quiet=False)

download_file(MOVIES_FILE_ID, "movies.pkl")
download_file(SIMILARITY_FILE_ID, "similarity.pkl")

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

if not isinstance(movies, pd.DataFrame):
    movies = pd.DataFrame(movies)

session = requests.Session()

import re

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id, title):
    if not API_KEY:
        return PLACEHOLDER_POSTER

    try:
     
        if pd.notna(movie_id):
            r = session.get(
                f"https://api.themoviedb.org/3/movie/{int(movie_id)}",
                params={"api_key": API_KEY, "language": "en-US"},
                timeout=8
            )
            if r.status_code == 200:
                poster = r.json().get("poster_path")
                if poster:
                    return "https://image.tmdb.org/t/p/w500" + poster

        clean_title = re.sub(r"[^a-zA-Z0-9 ]", "", title.lower())

        s = session.get(
            "https://api.themoviedb.org/3/search/movie",
            params={
                "api_key": API_KEY,
                "query": title,
                "language": "en-US",
                "include_adult": False
            },
            timeout=8
        )

        results = s.json().get("results", [])

        for movie in results:
            tmdb_title = movie.get("title", "").lower()
            tmdb_title = re.sub(r"[^a-zA-Z0-9 ]", "", tmdb_title)

            if clean_title == tmdb_title:
                poster = movie.get("poster_path")
                if poster:
                    return "https://image.tmdb.org/t/p/w500" + poster

     
        return PLACEHOLDER_POSTER

    except Exception:
        return PLACEHOLDER_POSTER




def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = similarity[index]

    movie_indices = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movie_indices:
        title = movies.iloc[i[0]]["title"]
        movie_id = movies.iloc[i[0]]["movie_id"]

        names.append(title)
        posters.append(fetch_poster(movie_id, title))

    return names, posters



st.title("🎬 Movie Recommendation System")
st.write("Select a movie and get similar recommendations")

selected_movie = st.selectbox(
    "Select a movie",
    movies["title"].values
)

if st.button("🎯 Recommend"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.caption(names[i])
            st.image(posters[i], use_container_width=True)
