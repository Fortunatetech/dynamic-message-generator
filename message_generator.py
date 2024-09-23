import os
from dotenv import load_dotenv
from groq import Groq
from placeholder_replacer import replace_placeholders
import streamlit as st

st.secrets["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] == st.secrets["GROQ_API_KEY"]

# Load API key from environment variables
load_dotenv()
KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=KEY)

# Root message template
TEMPLATE = """
Hi {Patient_name}! I tried calling you to discuss this, but I was unable to reach you. 
While processing your intake forms, I noticed that the requested spot with {Booked_Provider} is not available due to a scheduling conflict. 
However, {Alternative_Provider}, her colleague with similar credentials, is willing to manage {Booked_Provider}'s workload. 
If you are open to scheduling with {Alternative_Provider} at this same time- {Time} and this date {Date}, please let us know, and we will make the necessary adjustments to your schedule. 
We apologize for the inconvenience and would greatly appreciate your understanding.
"""

def generate_single_message(patient_name, booked_provider, alternative_provider, time, date):
    # Replace placeholders in the root template
    filled_template = replace_placeholders(
        TEMPLATE, patient_name, booked_provider, alternative_provider, time, date
    )
    
    # Construct the prompt to send to Groq
    prompt = f"""
    You are an expert message rewriter. Your task is to take the following message and generate one unique/
    variation of it that maintains the same meaning but uses different language:

    Message:
    {filled_template}

    Considers the below carefully:
    Ensure you generate a distinct, human-readable message.
    Ensure your the message you rewrite looks like human wrote it not a machine.
    Ensure You don not add preambles, follow the template given.
    Ensure the message is not too long.
    Do not use these kind of words/phrases:  reviewing your intake forms, flexibility
    """

    # Call Groq API to generate a unique response
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        model="llama-3.1-70b-versatile",
    )

    # Extract and return the single generated response
    generated_message = response.choices[0].message.content.strip()
    
     #Ensure proper spacing and structure
    formatted_message = generated_message.replace(". ", ".\n")  # Add line breaks after sentences for better readability

    return formatted_message
