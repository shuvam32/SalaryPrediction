import streamlit as st
import json
@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def defaultConfig(pagesize:int=0):
    if pagesize == 0:
        st.set_page_config(page_title="SalaryNode", page_icon="🤑", layout="wide")
    elif pagesize == 1:
        st.set_page_config(page_title="SalaryNode", page_icon="🤑", layout="centered")
        
    hide_st_style = """
                <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)