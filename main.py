import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=75406d4155df886fcca731454750f598&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_posters = []
    recommended_movies = []

    for j in movies_list:
        movie_id = movies.iloc[j[0]].movie_id

        recommended_movies.append(movies.iloc[j[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movie_posters


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Please enter the name of a movie', movies['title'].values)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[0])

    with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[1])

    with col3:
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[2])

    with col4:
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[3])

    with col5:
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[4])


footer = """<style>
a:link , a:visited {
color: 	rgb(192,192,192);
background-color: transparent;
text-decoration: none;
}

a:hover, a:active {
color: white;
background-color: transparent;
text-decoration: none;
}

.footer {
position: fixed;
bottom: 0px;
right: 0;
color: 	rgb(192,192,192);
text-align: right;
padding: 10px;
}
</style>
<div class="footer">
<p>Made with ❤ by <a href="https://github.com/FilterSinner" target="_blank">Ojal Binoj Koshy</a></p>
</div>
"""

st.markdown(footer,unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
            {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&q=80&w=1770&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;

}
[data-testid="stHeader"]{
    background-color:rgba(0,0,0,0);

}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)