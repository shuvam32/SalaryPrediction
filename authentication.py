import streamlit as st
from db import loadDb
from firebase_admin import auth
from helper import load_lottiefile
from streamlit_lottie import st_lottie



db = loadDb()
def app():
# Usernm = []
    col1, col2 = st.columns(2)
    with col1:
        st.header('Get Started !!')
        st.write("Sign Up and Logging to access our services")

    with col2:
        lottieRoadMap = load_lottiefile("./anima/Login.json")
        st_lottie(lottieRoadMap, width=200, height=150,key="Lottie_prediction", quality="max", speed=1)

    def f(email): 
        try:
            print(email)
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            
            global Usernm
            Usernm=(user.uid)
            
            st.session_state.signedout = True
            st.session_state.signout = True    
  
            
        except: 
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''


        
    
        
    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    
        

        
    
    if not st.session_state["signedout"]: # only show if the state is False, hence the button has never been clicked
        choice = st.selectbox('Login/Signup',['Login','Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password',type='password')
        
        if choice == 'Sign up':
            username = st.text_input("Enter  your unique username")
            type = st.selectbox('select',['student','employee'])
            
            if st.button('Create my account'):
                user = auth.create_user(email = email, password = password,uid=username)
                data ={"username": username, "email":email,"type":type}
                db.collection('users').document().set(data)
                
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                
        else:         
            if st.button('Login'):
                print("email",email)
                f(email)
            
    if st.session_state.signout:
                st.text('Name: '+st.session_state.username)
                st.text('Email id: '+st.session_state.useremail)
                st.write("You are Logged In")
                st.button('Sign out', on_click=t) 
                            
    def ap():
        st.write('Posts')