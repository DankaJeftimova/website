import streamlit as st
st.set_page_config(layout="wide")


col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

with col1:
    st.page_link("Home.py", label="Home")

with col2:
    st.page_link("pages/Education.py", label="Education")

with col3:
    st.page_link("pages/Projects.py", label="Projects")

with col4:
    st.page_link("pages/Certifications.py", label="Certifications")

with col5:
    st.page_link("pages/Competitions.py", label="Competitions")

with col6:
    st.page_link("pages/Erasmus.py", label="Erasmus+")

with col7:
    st.page_link("pages/Hobbies.py", label="Hobbies")

with col8:
    st.page_link("pages/Contact.py", label="Contact")



st.write("")
st.write("")
st.write("")



st.markdown("""
    <style>
    body {
        background-color: #0b1d3a;
        color: white;
    }

    .contact-form {
        max-width: 500px;
        margin: 0 auto;
        padding: 30px;
        background-color: #A569BD;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        font-family: Arial, sans-serif;
        color: white;
    }

    .contact-heading {
        text-align: center;
        color: black;
        font-size: 28px;
        margin-bottom: 20px;
        font-weight: bold;
        font-family: Arial, sans-serif;
    }

    .contact-form input[type="text"],
    .contact-form input[type="email"],
    .contact-form textarea {
        width: 100%;
        padding: 12px;
        margin-top: 8px;
        margin-bottom: 16px;
        border: 1px solid #ccc;
        border-radius: 8px;
        box-sizing: border-box;
        font-size: 16px;
        background-color: #6C3483;
        color: white;
    }

    .contact-form input::placeholder,
    .contact-form textarea::placeholder {
        color: #d0d0d0;
    }

    .contact-form textarea {
        height: 150px;
        resize: vertical;
    }

    .contact-form button {
        background-color: #4CAF50;
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }

    .contact-form button:hover {
        background-color: #45a049;
    }
    </style>

    <p class="contact-heading">Get in touch with me</p>

    <form class="contact-form" action="https://formsubmit.co/danka.i.jeftimova@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
""", unsafe_allow_html=True)
