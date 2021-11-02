import streamlit as st
import pandas as pd
import plotly.express as px

sidebar = st.sidebar

sidebar.title("Sidebar Title Here")
btn1 = sidebar.button("Get Balloons")

if btn1:
    st.balloons()

st.title("Streamlit App")
name = st.text_input("Enter your name")
btn = st.button("Submit")

if btn:
    st.text(f"You entered name {name}")


st.image('coin.jpg', use_column_width=True)

df = pd.read_csv('Pokemon.csv')


st.dataframe(df)
fig = px.bar(data_frame=df, x='Name', y='Speed', color='Type 1')
st.plotly_chart(fig, use_container_width=True)

# -------Code copied with python script--------