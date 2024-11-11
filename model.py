import streamlit as st
import joblib

@st.cache_resource
def load_models():
    linear_regression_model = joblib.load("./lr.pkl")
    decision_tree_model = joblib.load("./dt.pkl")
    random_forest_model = joblib.load("./rf.pkl")
    job_list = joblib.load("./job.pkl")
    scaler = joblib.load("./scaler.pkl")
    return linear_regression_model, decision_tree_model, random_forest_model, job_list, scaler