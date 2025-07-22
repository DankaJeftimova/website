import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(layout="wide")
from PIL import Image


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


imageme = Image.open("r.png")


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.title("Danka Jeftimova")
        st.write("High school student in the Mathematics-Computer Science High School - Skopje")
        st.write('An ambitious student from North Macedonia with excellent academic performance, numerous competition achievements, and a passion for programming. I am constantly investing in my education with the goal of contributing to the improvement of the society I live in. I created this website both as a learning opportunity and as a platform to share my accomplishments with the world. Feel free to explore the different pages to learn more about my education, projects, and interests. If you have any questions about my projects, achievements, or anything else, don’t hesitate to reach out through the contact form in the Contact page.')

    with right_column:
        st.image(imageme)



 