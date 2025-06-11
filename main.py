# Using streamlit for the user interface
import streamlit as st
# Using this to be able to load in pdf files
import PyPDF2

import io
import os
from openai import OpenAI

from dotenv import load_dotenv

# Loading in resources from .env file
load_dotenv()

# Configure name of tab/page/website
st.set_page_config(page_title="AI Resume Critiquer", page_icon="📄", layout="centered")

# Streamlit allows automatic rendering
# Anytime something changes the whole python script will re-run to render updated changes

# Writing title on the screen
st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

# Loading in API key to pass into OpenAI module, initialize LLM
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create elements on screen for inputting in resume and extra detail through text
# If either change values, script will re-run, but current value/state stored
uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf","txt"])
job_role = st.text_input("Enter the job role you're targetting (optional)")

# Creating a button to start analyzing resume, will equal True if button pressed
# Default value is false
analyze = st.button("Analyze Resume")

# Take in pdf file, load it in using module
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    # Make text string
    text = ""
    # Load in all the text on each page of the resume, add to text string
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Create function to get the text from the resume
# LLM won't be able to accept file with current semantics so pass only text to LLM
def extract_text_from_file(uploaded_file):
    # Check if pdf file
    if uploaded_file.type == "application/pdf":
        # Take uploaded file, convert read information into bytes object to load in through pdf reader module
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    # If not pdf, must by txt file, so can just read and decode
    return uploaded_file.read().decode("utf-8")
    
    
# When button pressed
if analyze and uploaded_file:
    try:
        # Will get a text string regardless of pdf or txt file
        file_content = extract_text_from_file(uploaded_file)
        
        # If any empty characters (no content) after removing beginning and ending whitespace
        if not file_content.strip():
            # Diplay error, stop program
            st.error("File does not have any content...")
            st.stop()
            
        # Pass text to LLM and receive critiques
        prompt = f"""Please analyze this resume and provide constructive feedback. 
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job applications'}
        
        Resume content:
        {file_content}
        
        Please provide your analysis in a clear, structured format with specific recommendations."""
        
        # Creating client to access OpenAI LLM
        client = OpenAI(api_key=OPENAI_API_KEY)
        # Directly envoke LLM, generates response
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                # System message is not something it's directly replying to
                # This is more for context the model needs
                {"role": "system", "content": "You are an expert resume reviewer with years of experience in HR and recruitment."},
                # Now inputting the prompt message on behald of the user, created above
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        # Print out response
        st.markdown("### Analysis Results")
        # There can be multiple messages given by LLM, taking only the first one (index 0)
        st.markdown(response.choices[0].message.content)
        
    except Exception as e:
        st.error(f"An error has occured: {str(e)}")

