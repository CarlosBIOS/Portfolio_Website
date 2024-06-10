import streamlit as st
import pandas

st.set_page_config(layout='wide')  # Dá para usar no telemóvel

col1, col2 = st.columns(2)
data: dict = pandas.read_csv('data.csv', sep=';').to_dict()
print(data)

with col1:
    st.image('Images/photo.png', width=460)

with col2:
    st.title('Ardit Sulce')
    st.info('Hi, I am Ardit! I am a programmer, teacher, and a founder of PythonHow. I graduated in 2013 with a Master'
            ' of Science in Geospatial Technologies from the University of Muenster in Germany with a focus on using'
            'Python for remote sensing. I have worked with companies from various countries, such as the Center for '
            'Conservation Geography, to map and understand Australian ecosystems, image processing with the Swiss '
            'in-Terra, and perfoming data mining to gain business insights with the Australian Rapid Intelligence.')

st.write('\nBelow you can find some apps I have built in python. Feel free to contact me!')
col3, _, col4 = st.columns([1.5, 0.4, 1.5])

with col3:
    for index in range(0, 20, 2):
        st.header(data['title'][index])
        st.image(f'Images/{data['image'][index]}', width=600)
        st.write(data['description'][index])
        st.write(f'[Source Code]({data['url'][index]})')
with col4:
    for index in range(1, 20, 2):
        st.header(data['title'][index])
        st.image(f'Images/{data['image'][index]}', width=600)
        st.write(data['description'][index])
        st.write(f'[Source Code]({data['url'][index]})')
