import streamlit as st

st.title("streamlit demo")

st.write("Choose")

data_name=st.sidebar.selectbox("Select", ("A","B"))

def get_data(data_name):
    if data_name=="A":
        st.write("Selected A")
    elif data_name=="B":
        st.write("Selected B")

get_data(data_name)