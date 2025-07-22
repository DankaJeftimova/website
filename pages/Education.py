import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(layout="wide")

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


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




with st.container():
    leftc, rightc = st.columns(2)
    with leftc:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown(
    """
    <div style='text-align: center;'>
        <h3>MY EDUCATION</h3>
    </div>
    """,
    unsafe_allow_html=True
)       
        st.write("")
        st.write("")
        st.write("I graduated from elementary school in my hometown with a perfect GPA of 5.00. After that I enrolled in the state school for Mathematics and Computer Science where I am currently a fourth year student. Learn more below.")
    with rightc:
        lottie_animation = load_lottie_file("learn.json")
        st_lottie(lottie_animation, height=300)


st.write("")
st.write("")

with st.container():
    left, right = st.columns(2)

    with left:
        with st.expander("Elementary education"):
            st.write('I went to "Sts. Cyrilus and Methodius - Kocani" elementary school, where I spent nine years studying a variety of subjects. It was there that I discovered my passion, first for math, and later for programming. With the support of my teachers, I developed my talent in both fields, demonstrated my knowledge, and proudly represented my school and city in various competitions. You can learn more about this on the Competitions page. Always a neat and responsible student, I maintained a perfect GPA of 5.0 at the end of every school year. Through friendships and valuable lessons, I grew both personally and academically, and I graduated in 2022.')

    with right:
        with st.expander("High school education"):
            st.write('Considering my love for programming and math, I decided to enroll in the state "Mathematical - Computer Science High School", after achieving great success on my entrance exams in math and physics. There, I had the opportunity to study a curriculum specifically designed for talented students. I explored complex mathematical subfields and learned new programming languages such as C++ and Python, starting from beginner level and progressing to more advanced topics like object-oriented programming. I also learned markup languages like HTML and CSS. Once again, with the support of my teachers and classmates, I excelled in national competitions, proudly representing my school. Since this high school is located in Skopje and I don’t live there, I moved into a state dormitory for high school students. You can read more about that below.')
            with st.expander("Dorm Life"):
                st.write('Moving to the high school student dorm "Zdravko Cvetkovski", I found a second family. Living together with kids from all over the country has been a truly wonderful experience. Among my new dormmates were also some of my classmates. This gave us the opportunity to support each other, both academically and personally. Together, we grew into independent, caring individuals who are always there to help one another. Dorm life is something unforgettable, and something I wish everyone could experience.')


