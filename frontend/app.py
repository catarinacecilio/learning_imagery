import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import imgkit
from PIL import Image
from dotenv import load_dotenv

# Set page tab display
st.set_page_config(
   page_title="Learning from Imagery 📸",
   page_icon= '🐧',
   layout="wide",
   initial_sidebar_state="expanded",
)

    # Example local Docker container URL
    # url = 'http://api:8000'
    # Example localhost development URL
    # url = 'http://localhost:8000'
    # load_dotenv()
    # url = os.getenv('API_URL')

st.title("Learning yellow Imagery 📸")

st.subheader("")
st.subheader("")

st.subheader("""Do you want to know how many peguins are nesting?
##
## Upload your photo here 👇 
""")

st.subheader("")


img_file_buffer = st.file_uploader('Upload an image')

if img_file_buffer is not None:

  col1, col2 = st.columns(2)

  with col1:
    ### Display the image user uploaded
    st.image(Image.open(img_file_buffer), caption="Here's the image you uploaded ☝️")

  with col2:
    with st.spinner("Wait for it..."):
      ### Get bytes from the file buffer
      img_bytes = img_file_buffer.getvalue()

      ### Make request to  API (stream=True to stream response as bytes)
      res = requests.post(url + "/upload_image", files={'img': img_bytes})

      if res.status_code == 200:
        ### Display the image returned by the API
        st.image(res.content, caption="Image returned from API ☝️")
      else:
        st.markdown("**Oops**, something went wrong 😓 Please try again.")


st.subheader("""
##
##
""")

# Dataset
st.write("🐧 dataset used 🐧[link] (https://www.robots.ox.ac.uk/~vgg/data/penguins/)")

