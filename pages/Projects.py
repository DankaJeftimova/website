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



st.write("")
st.write("")
st.write("")




image1 = Image.open("blender1.jpg")
image2 = Image.open("blender3.jpg")
image3 = Image.open("blender2.jpg")
image4 = Image.open("render.png")
viz = Image.open("vizz.png")

width = 300
height = 200

image1 = image1.resize((width,height))
image2 = image2.resize((width,height))
image3 = image3.resize((width,height))
image4 = image4.resize((width,height))
viz = viz.resize((width,height))

title = """<div style = "text-align: center;">
<h2>Programming languages and my experience with them. Projects I have built </h2></div>"""

st.markdown(title,unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")


with st.expander("This Website"):
    st.write("This website is my biggest project to date. I built it using Python and Streamlit. I used various different modules, like Pillow for image processing. A little bit of HTML and CSS was used — mainly for the creation of the contact form and to add some fine styling details. The Lottie Files library was used to include animations. Consisting of 8 pages, this website showcases my skills, achievements, and the projects I’ve worked on so far. I’m proud of how it turned out, and I hope to keep updating it with more of my work and accomplishments.")

st.write("---")


with st.expander("Programming Languages"):
    with st.expander("C++"):
        st.write("I started learning C++ in 7th grade of elementary school. I noticed that I enjoy programming, so I continued learning the language by myself. I was 12 years old at the time. At 14, I started my first year of high school and continued learning C++. In the third year of high school, I learned object-oriented programming with C++ and practiced some advanced topics like inheritance and polymorphism. I use the C++ language mostly in competitive programming. C++ introduced me to most programming concepts, from beginner-level stuff like if statements, loops, and variables, to advanced topics like OOP, graph algorithms, vectors, and the like. I built my logic and problem-solving skills by practicing competitive programming problems on websites like Mendo, Codeforces, CSES and LeetCode. Across all of these websites, I have solved more than 380 problems.")

    with st.expander("Python"):
        st.write("I started learning Python when I was 16. After finishing my second year of high school, I took a free online Harvard course about programming in Python. It was very easy to transition from C++. I completed all of the assignments and created a final project: a console game where you can choose to play Tic Tac Toe, Hangman, or Guess the Number. You can learn more about it in the Project section of this page.")
        st.write("After that, I chose an Intelligent Systems class in high school, where we learned how to implement AI algorithms like BFS, DFS, A* Search, Minimax, and others. We also began learning some basics of machine learning.")
        st.write("At the end of the school year, we worked in teams to build a final project. My team created an intelligent system that recommends clothing. It uses K-Means to classify the data. You can learn more about it in the Project section of this page.")
        st.write("This website was also built using Python, more about that in the This Website section above.")

    with st.expander("HTML and CSS"):
        st.write("In the third year of high school, we started learning a little bit of web design. That was when I got my first experience with the two markup languages. We built a lot of websites using just HTML and CSS to become familiar with them. A little bit of HTML and CSS is also used in this website, you can learn how and where in the This Website section above. In the fourth year (starting this September), I hope to learn more HTML and CSS in an elective subject I chose called Web Design.")

    with st.expander("SQLite"):
        st.write("By joining the virtual camp Kode with Klossy – Data Science (learn more on the Certifications page), I had the opportunity to learn a little bit of SQLite. We started with some basic queries and moved on to subqueries and more advanced concepts like joins. I am still a beginner in this language, but I hope to advance my skills by making my own projects and taking an advanced SQL course in the future.")



with st.expander("Projects"):
    with st.expander("Harvard CS50 Python Project"):
        left, right = st.columns(2)
        with left:
            st.write("To complete the CS50P course (see more on the Certifications page), I had to create a final project. The project had to include multiple files, a testing file using pytest, and a README written in Markdown with at least 1000 words explaining what the code does and how it works. For my project, I built a console application where users can choose between playing Tic Tac Toe (in two modes: against the computer or another player), Guess the Number, and Hangman. I used exception handling to manage user input errors, and I made it possible to exit the game at any time. To demonstrate how the project works, I recorded a video (shown on the right) as part of the final submission. This project gave me valuable experience with Python, and I really enjoyed building it.")
        with right:
            st.video("CS50P.mp4",width=400)

    with st.expander("Clothes recommendation system with Python and KMeans algorithm"):
        ll,rr = st.columns(2)
        with ll:
            st.write("In my third year of high school, I took an elective subject called Intelligent Systems. For the end-of-year project, we worked in a team to develop an intelligent system. Our system provided clothing recommendations based on user input. We trained it using a dataset, and it continued learning over time from user interactions and data, in addition to the original dataset. The system classified data using the KMeans++ algorithm. We also built a simple login system with username and password functionality, and designed a basic GUI using Tkinter. This was a great project to work on, I really enjoyed the teamwork and learning how to apply KMeans in a real application. A video demonstrating how the system works is shown on the right.")
        with rr:
            st.video("vid.mp4")
    with st.expander("Kode with Klossy Data Science Project"):
        k1, k2 = st.columns(2)
        with k1:
            st.write('We worked in a team for our final Kode With Klossy project. We had to analyze data from online datasets of our choosing and visualize it to make it easier for people to interpret. Our project, named "Fashion\'s Footprint" focused on how fast fashion harms the environment. From CO2 emissions to waste in the oceans, we showcased the damage fast fashion causes through our dashboard, which included three visualizations, an introduction, and a data analysis. Created in Tableau, working on this dashboard helped us explore more of Tableau’s features and practice teamwork.')
        with k2:
            st.image(viz)


    with st.expander("3d design of my room with Blender"):
        left2, right2 = st.columns(2)
        with left2:
            st.write("")
            st.write("")
            st.write("")
            st.write("As part of the computer science course in my second year of high school, we studied 3D graphics and learned how to use Blender. For our end-of-semester project, we had to create a 3D model of our own room. I used photos of the actual materials in my room to recreate them as textures on the objects in the model. I also did some additional learning on my own to accurately model all the objects. Attached are photos showing the modeling process and a final rendered image of the room.")
        with right2:
            ll, rr = st.columns(2)
            with ll:
                st.image(image1)
                st.image(image2)
            with rr:
                st.image(image3)
                st.image(image4)