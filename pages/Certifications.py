import streamlit as st
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



width = 450
height = 350

grad = Image.open("graduation.png")
grad = grad.resize((width,height))


st.write("")
st.write("")
st.write("")




title = """<div style = "text-align: center;">
<h2>Certifications</h2></div>"""

st.markdown(title,unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")


with st.expander("Harvard CS50's Introduction to Programming with Python"):
    st.write("Through this free course, I had the opportunity to learn Python. I already had a lot of programming experience, but learning new things is always enjoyable. I covered the basics, variables, functions, dictionaries, and lists, as well as some more advanced topics, such as testing with pytest, importing modules, and basic photo processing. After each lesson, we were given a problem to solve and submit. At the end of the course, I had to complete and submit a final project, you can read more about it in the Projects section. I completed this course in 2024. If you would like to see this certification, please contact me using the form on the Contact page.")
    st.link_button("CS50P","https://pll.harvard.edu/course/cs50s-introduction-programming-python")
with st.expander("Kode With Klossy data science virtual camp"):
    k1, k2 = st.columns(2)
    with k1:
        st.write("In the summer of 2025, I had the opportunity to participate in the Kode With Klossy Data Science virtual camp. There, I learned the basics of SQLite and Tableau, and had the chance to connect with people from all over the world. Through Culture of Tech sessions, I explored the latest trends in technology and learned how to stay informed and engaged in the field. I also received valuable advice from professionals working in tech. As a Kode With Klossy alumna, I now have access to a supportive community, ongoing resources, and mentorship that continues to inspire my tech journey. During the camp, I worked on a team to create a final project, which involved analyzing real-world data and presenting our findings through interactive Tableau dashboards. You can learn more about our final project on the Projects page. If you would like to see this certification, please contact me using the form on the Contact page.")
        st.link_button("Kode With Klossy","https://www.kodewithklossy.com/")
    with k2:
        st.image(grad)

with st.expander('Thesis on "Biocomputers and DNA Programming: Using the Code of Life"'):
    st.write('The Mathematical Union, the Programming Union, and the Ministry of Arts and Sciences organized a student science conference. To be invited, you had to submit a thesis on a topic in computer science or mathematics, with the computer science topic requiring the inclusion of code. If your thesis was accepted, you would be invited to present it in Ohrid. I am a co-author of a thesis that was accepted. A schoolmate and I wrote a paper on biocomputers, titled "Biocomputers and DNA Programming: Using the Code of Life." After introducing what biocomputers are and how they work (including paragraphs and code on logic gates), we explored potential applications of biocomputers and the ethical concerns surrounding them. We also wrote a Python simulation to demonstrate how a simple addition problem could be encoded in a biocomputer. We were inspired by the fact that this year marked the first time a biocomputer became commercially available. We are excited to see where technology will go with biocomputers. If you would like to see this certification, please contact me using the form on the Contact page.')

with st.expander("GDHT 2024"):
    st.write("Game Design How To was a free workshop where we learned how the game design process begins. We worked in Unreal Engine and created a simple game in which the player drives a car through a field. If you would like to see this certification, please contact me using the form on the Contact page.")


