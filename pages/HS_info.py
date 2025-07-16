import streamlit as st
import pandas as pd
import requests
st.title("Highschool applying to colleges")

url = "https://didactic-xylophone-r4wpg95j964p3xgqw.github.dev/"

data = requests.get(url).json()

st.json(data, expand=True)