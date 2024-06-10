import streamlit as st
from send_emails import send_emails

# E vai ser preciso um email e uma pass:
# O email que foi criado para recber os emails: portfoliowebsitepython@gmail.com
# A pass vai ser gerada, para não colocar a pass original no código: fui à minha conta Google e procurei por apps
# passwords e criei uma pass com o nome Portfolio Website: whbb qmgg ixbu hbgg

st.header('Contact Me')

with st.form(key='email_forms'):
    user_email = st.text_input('Your email Address')  # Just write 1 line!!
    user_message = st.text_area('Write your message')  # We can write multiples lines!!
    button = st.form_submit_button('Submit')
    if button:
        message = f"""\
Subject: Email from the Portfolio Website 
        

From: {user_email}
{user_message}
"""
        send_emails(message)
        st.info('Your email was succefully send it')
