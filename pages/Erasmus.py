import streamlit as st
from streamlit_lottie import st_lottie
import json
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



image1 = Image.open("all.jpg")
image2 = Image.open("me.jpg")
image3 = Image.open("all_in_circle.jpg")

width, height = [3000, 2500]

image1 = image1.resize((width,height))
image2 = image2.resize((width,height))
image3 = image3.resize((width,height))

image4 = Image.open("with_the_tape.jpg")
image4 = image4.resize((width,height))

image5 = Image.open("all_romania.jpg")
image5 = image5.resize((width,height))

image6 = Image.open("me_debating.jpg")
image6 = image6.resize((width,height))

st.set_page_config(layout="wide")

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


with st.container():
    left, right = st.columns(2)
    with left:
        st.write("")
        st.write("") 
        st.write("")
        st.write("")
       
        st.markdown("""
                    <div style='text-align: center;'>
                    <h3>ERASMUS+</h3>
                     </div>
                    """,unsafe_allow_html=True) 
        st.write("")
        st.write("")
        st.write("Erasmus+ projects are a wonderful opportunity for growth and intercultural integration. By participating in these projects, I had the chance to learn, connect, debate and share my culture with different people from all over the world. Below you can find details about my contributions to these projects as well as what they taught me.")
    with right:
        animation = load_lottie_file("erasmus.json")
        st.lottie(animation, height=300)


with st.expander('Youth Exchange "Digitally United"'):
    st.write("Where: Brebu, Romania")
    st.write("When: 04.12.2024 - 13.12.2024")
    st.write("Certification: Youthpass")
    st.write("About the project: Empowering youth through virtual tools, AI, and technology, this initiative builds skills, fosters media literacy, and strengths community engagement. Participants explore how digital innovations can enhance communication, drive creativity, and address social challenges through interactive workshops and collaborative projects. Aligned with Nevo Parudimos' mission of inclusion and education, it promotes cultural diversity, volunteerism, and youth development in a positive, tech driven way.")
    st.write("My experience: By participating in the youth exchange in Romania, I had the amazing opportunity to represent my country and learn alongside people from many different cultures. The project focused on the responsible use of AI, which opened my eyes to both the benefits and the ethical challenges of new technologies. Through workshops, debates, and a collaborative video project, I gained valuable skills in critical thinking and digital responsibility. One of the best parts of the experience was getting to know the traditions, languages, and perspectives of the other participants. Living and learning together helped us build strong connections that went beyond borders. Exploring Romania and its culture was a beautiful journey that I will always remember.")
    st.write("What I learned: During this project, I developed all 8 Erasmus competences: Literacy competence, multilingual competence, mathematical and STEM competence, digital competence, personal, social and learning to learn competence, citizenship competence, entrepreneurship competence, and cultural awareness and expression competence. I practiced team building, communicating using the English language, and compromise. I learned how to use Kahoot and Canva to make fun quizzes, and presentations about my country. I used Kdenlive for video editing that was needed for the final collaborative project: a video raising awareness about responsible AI use. I practiced debating, by participating in a debate about the good and bad sides of AI. Overall I contributed to the non-formal learning environment and I got to learn a lot of new things.")
    col11, col21, col31 = st.columns(3)
    with col11:
        st.image(image4)
    with col21:
        st.image(image5)
    with col31:
        st.image(image6)

with st.expander('Youth Exchange "The Art of Games"'):
    st.write("Where: Placzewo, Poland")
    st.write("When: 13.06.2025 - 22.06.2025")
    st.write("Certification: Youthpass")
    st.write("About the project: About the project: The Youth Exchange brought together young people from different countries who are interested in art and games. Through interactive workshops, simulations, and group activities, participants gained valuable knowledge, skills, and tools that will support their personal development and are useful for effective group work. Participants played games introduced by their foreign peers, programmed games using AI tools, explored different forms of art and the rich cultures of each participating country.")
    st.write("My experience: By participating in the youth exchange &quot;The Art of Games&quot;, I got the opportunity to represent my country, my culture, and my knowledge in art and games, with a group of wonderful people from 6 different countries. This experience taught me a lot of new things about friendship, team building and living together with different people. The connections I made are special and something I will keep with me forever. Discovering the country of Poland and its people was a beautiful and magical adventure.")
    st.write("What I learned: During this project, I gathered a lot of new knowledge. I developed all 8 Erasmus competences: Literacy competence, multilingual competence, mathematical and STEM competence, digital competence, personal, social and learning to learn competence, citizenship competence, entrepreneurship competence, and cultural awareness and expression competence. I practiced team building, communicating using the English language, finding similarities between languages as well as how to present my culture in an interesting and fun way. I got even more experience in how it feels to live with people from different countries and how to communicate and compromise.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(image1)
    with col2:
        st.image(image2)
    with col3:
        st.image(image3)