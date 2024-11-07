import streamlit as st
from hadith.models import Post
import pandas as pd
import requests
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deen.settings')

django.setup()
# Fetch data from Django's REST API
def fetch_data():
    response = requests.get("http://localhost:8000/hadith/posts/")
    return response.json() if response.status_code == 200 else None
queryset=Post.objects.all().values()
data_list=list(queryset)
dataframe=pd.DataFrame(data_list)
# st.title("Streamlit Dashboard")
st.title('Testin Streamlit integration with django')
data = fetch_data()

if data:
    st.write("Data from Django:")
    st.write(data)
else:
    st.error("Failed to fetch data.")



if dataframe:
    st.write('Posts :-')
    st.write(dataframe)
else:
    st.error('dataframe is empty')