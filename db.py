import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

@st.cache_resource
def loadDb():
    cred = credentials.Certificate("./firebase.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db