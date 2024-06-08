import streamlit as st
from os import path
from PIL import Image

st.set_page_config(layout='wide')  # Dá para usar no telemóvel
st.title('Home')
img = Image.open('Images/1.png')
st.image(img)
