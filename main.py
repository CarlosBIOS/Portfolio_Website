import streamlit as st
from os import path
from PIL import Image
import pandas

st.set_page_config(layout='wide')  # Dá para usar no telemóvel
st.title('Home')
img = Image.open('Images/1.png')
st.image(img)

data = pandas.read_csv('data.csv')
print(data)
