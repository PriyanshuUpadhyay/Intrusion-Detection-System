import streamlit as st
from predict import predict_page
from explore import explore_page
from simulate import simulate_page

side = st.sidebar.selectbox("Predict, Explore or Simulate",("Predict","Explore", "Simulate"))

if(side == "Predict"):
    predict_page()
elif(side == "Simulate"):
    simulate_page()
else:
    explore_page()