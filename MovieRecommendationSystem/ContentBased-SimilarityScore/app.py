#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
#streamlit library is used to convert task into webapplication


# In[15]:


import pickle
import pandas as pd

def recommendation(movie):
    movie_index = movies_dict[movies_dict['original_title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1:6]
    
    recommended_movies =[]
    
    for i in movie_list:
        recommended_movies.append(movies_dict.iloc[i[0]].original_title)
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

#title for the webpage
st.title('Movie Recommeder System')

#options on the webpage
option = st.selectbox('Select your Movie:',movies['original_title'].values)

#button for recommend
if st.button('Recommend'):
    recommendations = recommendation(option)
    for i in recommendations:
        st.write(i)
    


# In[ ]:




