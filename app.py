from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables and configure API
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro Vision
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(image, prompt):
    response = model.generate_content([image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title='AI-Powered Medical Image Explorer', layout="wide")
st.markdown("""
    <p style='font-family: "Comic Sans MS", cursive, sans-serif; color: black; font-size: 22px;'>
        ✨ Designed by Athar ✨
    </p>
    """, unsafe_allow_html=True)




# Custom CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")  # Assuming you have a 'style.css' file for custom styles

st.title('AI-Powered Medical Image Explorer')

uploaded_file = st.file_uploader("Upload a Medical Image (X-ray, MRI, etc.)", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Medical Image.", use_column_width=True)
    image_data = input_image_details(uploaded_file)

    submit = st.button("Analyze Image")

    if submit:
        # Define a prompt for medical image analysis
        medical_analysis_prompt = "Analyze this medical image and provide insights or findings."

        response = get_gemini_response(image_data, medical_analysis_prompt)
        st.subheader("Analysis Results")
        st.write(response)

# Add author name in a smaller font size at the bottom

