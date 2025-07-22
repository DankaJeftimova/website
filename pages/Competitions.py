import streamlit as st
from streamlit_lottie import st_lottie
import json
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




def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)



with st.container():
    left, right = st.columns(2)
    with left:
        animation = load_lottie_file("competitions.json")
        st.lottie(animation, height = 300)

    with right:
        st.write("")
        st.write("")
        st.write("")
        st.markdown(
    """
    <div style='text-align: center;'>
        <h3>COMPETITIONS</h3>
    </div>
    """,
    unsafe_allow_html=True
)       
        st.write("")
        st.write("")
        st.write("Ever since first grade of elementary school, I have had a competitive spirit which drove me to take part in multiple competitions over the years. Starting with logic and mathematics and making my way to computer science has been a wonderful journey, proven by my various achievements presented below.")


st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

left, lm, middle, mr, right = st.columns(5)




with left:
    st.write("Math Competitions")
    st.write("- Participation in the Macedonian Math Olympiad 2024")
    st.write("- Second National Award 2024")
    st.write("- First City Award 2024")
    st.write("- Second Regional Award 2023")
    st.write("- Third City Award 2023")
    st.write("- Participation in National Competition 2022")
    st.write("- Third Regional Award 2022")
    st.write("- Third Regional Award 2020")
    st.write("- First City Award 2020")
    st.write("- Third Regional Award 2019")
    st.write("- First City Award 2019")
    


with middle:
    st.write("Programming competitions")
    st.write("- Participation in a competition for choosing a girls' team")
    st.write("- Third National Award 2025")
    st.write("- Third Regional Award 2025")
    st.write("- Third National Award 2024")
    st.write("- Third Regional Award 2024")


with right:
    st.write("Other Competitions")
    st.write('- Third Award at the international comeptition "Kengur" 2015')
    st.write('- Second Place at the international comeptition "Kengur" 2014')