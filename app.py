import streamlit as st
from PIL import Image
import pandas as pd

# Sidebar contents
st.sidebar.title("KNU Top AI")
img = Image.open("logo.jpg")
st.sidebar.image(img)
