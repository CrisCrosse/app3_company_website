import streamlit as st
from send_email import send_email

st.header("Contact us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address:")

    topic_options = ("Job Enquiry", "Project Proposal", "Other")
    topic = st.selectbox("Email Topic", topic_options)

    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New {topic} email from {user_email}

From {user_email}
{raw_message}
"""

    button = st.form_submit_button("Submit")
    print(button)
    # button is true when button is pressed
    if button:
        #print("submit button pressed")
        send_email(message)
        st.info("Your email has been sent")
        