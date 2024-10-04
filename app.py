##IMPORTING the libraries
import streamlit as st 
import google.generativeai as genai 
from langchain import PromptTemplate,LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI



## Set up local environment
import os 
from dotenv import load_dotenv 
load_dotenv() #ACtivate the local envirionment
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

import os
os.environ['GOOGLE_API_KEY'] = "AIzaSyAzOfotbdOxJ6LJTht8daCw78p9yqgdW1U"  # Replace with your actual API key



## Designing the webpage
st.title("🌩️BOLT(Automated Movie Recommender System📽️)")
user_input=st.text_input("Enter The Movie Title,\Genre or Keyword🎞️")

# Create a prompt template for generating movie recommendations
prompt_template = PromptTemplate(
    input_variables=["user_input"],
    template="Based on the input '{user_input}', suggest some movies that I might enjoy.")

# Initialize the generative AI model
llm = ChatGoogleGenerativeAI(model="gemini-pro",api_key=os.getenv("GOOGLE-API-KEY"))

# When the user submits their input
if user_input:
    
    # Format the prompt with user input
    prompt = prompt_template.format(user_input=user_input)
    recommendations=llm.predict(text=prompt)
    # Display the recommendations in the Streamlit app
    st.write(f"Recommended Movies:\n{recommendations}")
else:
    st.warning("Please enter a movie title, genre, or keyword.")
        
