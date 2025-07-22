import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image

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



width = 300
height = 300

image1 = Image.open("hat.jpg")
image2 = Image.open("octopus.jpg")
image4 = Image.open("emb1.jpg")
image5 = Image.open("emb2.jpg")
image6 = Image.open("emb3.jpg")

image1 = image1.resize((width,height))
image2 = image2.resize((width,height))
image4 = image4.resize((width,height))
image5 = image5.resize((width,height))
image6 = image6.resize((width,height))



def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


with st.container():
    leftc, rightc = st.columns(2)
    with leftc:
        st.write("")
        st.write("")
        animation = load_lottie_file("Book.json")
        st.lottie(animation, height=300)
    with rightc:
        st.write("")
        st.write("")
        st.write("")
        st.markdown(
    """
    <div style='text-align: center;'>
        <h3>MY HOBBIES</h3>
    </div>
    """,
    unsafe_allow_html=True
)       
        st.write("")
        st.write("")
        st.write("In my free time, I enjoy immersing myself in books and exploring creative outlets like embroidery and crochet. These activities allow me to relax, express myself, and continually learn new techniques. Reading expands my perspective, while crafting brings a unique sense of calm. If you're curious, you can discover more about these interests further down.")
        st.write("")
        st.write("")
        




with st.expander("Books"):
    st.write('"That’s the thing about books. They let you travel without moving your feet." — Jhumpa Lahiri. I’ve always loved reading because it really does feel like a way to explore the world without going anywhere. Ever since I first learned how to read, I’ve been hooked. I started with space encyclopedias, I was obsessed with stars and planets, and then got into sci-fi, fantasy, mystery, and eventually classic books. I think classic literature is super important because it helps us understand how people lived and thought in the past. Whether I’m flipping through pages or listening to an audiobook, reading is one of my favorite ways to relax, learn, and get inspired.')



with st.expander("Embroidery"):
    left, right = st.columns(2)
    with left:
        st.write("")
        st.write("Embroidery is a way for me to express my creativity. Through detailed handiwork, I create illustrations of various subjects. I must admit, though, that I especially love embroidering flowers. I enjoy keeping myself busy with embroidery or crochet while listening to audiobooks. On the right are a few examples of my work.")
    with right:
        l,r,e = st.columns(3)
        with l:
            st.image(image4)
        with r:
            st.image(image5)
        with e:
            st.image(image6)

with st.expander("Crochet"):
    left, right = st.columns(2)
    with left:
        st.write("")
        st.write("")
        st.write("")
        st.write("")

        st.write("Crochet is another way for me to channel my creativity. Through intricate stitching, I create a variety of items, from cozy scarves to decorative pieces. Like embroidery, crochet allows me to relax and focus while listening to audiobooks. On the right are a few examples of my crochet work.")
    with right:
        l,r = st.columns(2)
        with l:
            st.image(image1)
        with r:
            st.image(image2)




