import streamlit as st

st.title("Upload image")
text_tab, upload_tab, cam_tab = st.tabs(["Text Input", "Upload Image", "Cam Input"])

with text_tab:
  st.title("Text Input")
  text_input = st.text_input("Enter text here...")
  if text_input:
    st.subheader("Here's what you entered: ")
    st.markdown("**{}**".format(text_input))

with upload_tab:
  file_uploader = st.file_uploader("Upload An Image", ["jpg", "jpeg", "png", "bmp"], help = "Upload an Image")
  if file_uploader:
    st.subheader("Here's what you uploaded: ")
    st.image(file_uploader)

with cam_tab:
  cam_uploader = st.camera_input("Take a picture")
  if cam_uploader:
    st.header("Here's what you took a picture of")
    st.image(cam_uploader)
