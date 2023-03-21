import streamlit as st
from io import StringIO
import imgkit
from PIL import Image
from dotenv import load_dotenv
import requests

# Set page tab display
st.set_page_config(
   page_title="Learning from Imagery 📸",
   page_icon= '🐧',
   layout="wide",
   initial_sidebar_state="expanded",
)

col1, col2, col3 = st.columns(3)
with col1:
    st.title("Learning :yellow[:orange[from]] :yellow[Imagery] 📸")

with col2:
    image = Image.open('bounding_box.png')
    st.image(image, caption='bouding box')

with col3:
    image = Image.open('pinguim_filhote.jpeg')
    st.image(image, caption='baby penguin')

    # Example local Docker container URL
    # url = 'http://api:8000'
    # Example localhost development URL
 url = 'http://localhost:8000'
    # load_dotenv()
    # url = os.getenv('API_URL')


st.subheader("""Do you want to count objects? Let's start with penguins!!! 🤓🔎
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
