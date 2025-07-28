import streamlit as st
import pickle 
import requests

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

model = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
titles = model['title'].values

def recommend(movie):
   index = model[model["title"]== movie].index[0]
   distance = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)
   rec = []
   rec2 = []
   for i in distance[1:6]:
        movies_id = model.iloc[i[0]].id
        rec.append(model.iloc[i[0]].title)
        rec2.append(fetch_poster(movies_id))
   return rec, rec2

st.header("Movie Recommendation System")
select = st.selectbox("Select movie from dropdown",titles)



if st.button("Recommend"):
    movie,poster= recommend(select)
    m1,m2,m3,m4,m5 = st.columns(5)

    with m1:
        st.text(movie[0])
        st.image(poster[0])
    with m2:
        st.text(movie[1])
        st.image(poster[1])
    with m3:
        st.text(movie[2])
        st.image(poster[2])
    with m4:
        st.text(movie[3])
        st.image(poster[3])
    with m5:
        st.text(movie[4])
        st.image(poster[4])
