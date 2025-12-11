import streamlit as st
from PIL import Image
import pandas as pd
from datetime import datetime



# Sidebar contents
st.sidebar.title("KNU Top AI")
img = Image.open("logo.jpg")
st.sidebar.image(img, width=40)

# //////////////////////////////////////////////////////////

st.title('KNU Top AI Dashboard')

now = datetime.now()
st.write(datetime(now.year, now.month, now.day))
<div style="text-align: right"> your-text-here </div>
