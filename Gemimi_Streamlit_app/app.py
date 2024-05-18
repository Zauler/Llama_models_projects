import os
from dotenv import load_dotenv

import streamlit as st
from PIL import Image
import google.generativeai as genai

load_dotenv()  # Load all the environment variables from .env

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro Vision 
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])
    return response.text 

def input_image_details(upload_file):
    if upload_file is not None:
        
        image_parts = [
            {
                "mime_type": uploaded_file.type, # Get the mime type of the up 
                "data": upload_file.getvalue()   # Read the file into bytes
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

### Initialize our streamlit app

st.set_page_config(page_title="Invoice Extractor")
st.header("Invoice Extractor")

input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg","jpeg","png"])
image = None

if uploaded_file:
    try:
        image = Image.open(uploaded_file)
        st.image(image,caption="Uploaded Image.", use_column_width=True)
    except Exception as e:
        st.error(f"Error loading image: {e}")
    
submit=st.button("Tell me about the invoice")

input_prompt="""
You are an expert in understanding invoices. We upload an image as an invoice
and you will have to answer any question based on the uploaded invoice image.
"""

# If submit button is clicked

if submit:
    if uploaded_file and input_prompt.strip():
        try:
            image_data = input_image_details(uploaded_file)
            response = get_gemini_response(input_prompt,image_data,input)
            if response:            
                st.subheader("The response is: ")
                st.write(response)
            else:
                st.error("Cound not get a response. Please try again.")
            
        except Exception as e:
            st.error(f"Error processing the request {e}")
    else: 
        st.error("Please upload an invoice image and provide a valid prompt.")
    