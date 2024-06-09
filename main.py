import streamlit as st
import csv

st.set_page_config(layout='wide')  # Dá para usar no telemóvel

col1, col2 = st.columns(2)
data: list = []

with open('data.csv', encoding='utf-8') as file:
    data_read = csv.reader(file)
    for row in data_read:
        if row != ['title;description;url;image']:
            data.append(row[0].split(';'))

print(data)

with col1:
    st.image('Images/photo.png', width=600)
    for index in range(0, 20, 2):
        st.title(data[index][0])
        st.image(f'Images/{data[index][3]}', width=600)
        st.write(data[index][1])
        st.write(data[index][2])

with col2:
    st.title('Ardit Sulce')
    st.info('Hi, I am Ardit! I am a programmer, teacher, and a founder of PythonHow. I graduated in 2013 with a Master'
            ' of Science in Geospatial Technologies from the University of Muenster in Germany with a focus on using'
            'Python for remote sensing. I have worked with companies from various countries, such as the Center for '
            'Conservation Geography, to map and understand Australian ecosystems, image processing with the Swiss '
            'in-Terra, and perfoming data mining to gain business insights with the Australian Rapid Intelligence.')
    for index in range(1, 20, 2):
        st.title(data[index][0])
        st.image(f'Images/{data[index][3]}', width=600)
        st.write(data[index][1])
        st.write(data[index][2])
