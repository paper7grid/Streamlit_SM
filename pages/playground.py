import pandas as pd
import streamlit as st

st.title("Playground")
st.subheader("Movie!")

movie = pd.read_csv("data/movie_metadata.csv")
st.dataframe(movie)