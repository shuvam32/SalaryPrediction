import streamlit as st
from helper import defaultConfig
defaultConfig()
import pandas as pd
from streamlit_lottie import st_lottie
from helper import load_lottiefile
from streamlit_extras.switch_page_button import switch_page

if 'username' not in st.session_state:
        st.session_state.username = ''
if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

headercol1, headercol2 = st.columns(2)

with headercol1:
        st.title("Salary Node :zap:")
        st.caption("Using an online tool can make it easier for you to employ your investigative skills to identify the culprit. centered on concepts like segment mapping and yolo for optimised target identification.")
with headercol2:
        lottieHomeLoader = load_lottiefile("./anima/home.json")
        st_lottie(lottieHomeLoader, width=200, height=200,key="lottie_homeLoader", quality="max", speed=1)

# Landing page title
st.header("Features we Offer",divider="rainbow")

col1, col2 = st.columns(2)

col3, col4 = st.columns(2)

with col1:
        lottieSalary = load_lottiefile("./anima/salary.json")
        st_lottie(lottieSalary, width=200, height=200,key="lottie_salary", quality="max", speed=1)
        st.header("Salary Prediction")
        st.write("Predict your salary based on various factors.")
        if st.button("Check", key="Salary_Perdictor_button"):
                switch_page("Salary_Perdictor")

with col2:
        lottieRoadMap = load_lottiefile("./anima/RoadMap.json")
        st_lottie(lottieRoadMap, width=200, height=200,key="lottie_RoadMap", quality="max", speed=1)
        st.header("Career Guidance")
        st.write("Check out our roadmap to Boost your carrier!")
        if st.button("Check", key="Road_Map_button"):
                switch_page("Road_Map")

with col3:
        lottieSocial = load_lottiefile("./anima/connect.json")
        st_lottie(lottieSocial, width=200, height=200,key="lottie_Social", quality="max", speed=1)
        st.header("Social Media Platform")
        st.write("Connect with professionals, post job openings, and apply for jobs!")
        if st.button("Check", key="Trending_Post_button"):
                switch_page("Trending_Post")
st.write("")
st.write("")

st.header(":mailbox: Get In Touch With US!", divider="rainbow")


contact_form = """
<form action="https://formsubmit.co/nevilpanchal5@gmail.com
" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
        
# Footer
st.header("Thank you for visiting our Salary Node!")

