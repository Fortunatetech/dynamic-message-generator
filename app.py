import streamlit as st
from message_generator import generate_single_message
import os

st.write("GROQ API KEY:", st.secrets["GROQ_API_KEY"])

st.write(
    "Has environment variables been set:",
    os.environ["GROQ_API_KEY"] == st.secrets["GROQ_API_KEY"],
)

# UI Layout using Streamlit columns
def main():
    st.set_page_config(layout='centered', page_title="Orenda Message Generator")
    st.title("Orenda Message Generator")

    # First row: 3 columns for Patient Name, Booked Provider, and Alternative Provider
    col1, col2, col3 = st.columns([ 2, 2, 2])

    with col1:
        patient_name = st.text_input("Patient Name")
    with col2:
        booked_provider = st.text_input("Booked Provider")
    with col3:
        alternative_provider = st.text_input("Alternative Provider")

    # Second row: Centralized Time and Date fields
    col4, col5 = st.columns([ 1, 1])  # Use column layout to centralize Time & Date
    with col4:
        time = st.text_input("Time")
    with col5:
        date = st.text_input("Date")

    if st.button("Generate Dynamic Message"):
        if patient_name and booked_provider and alternative_provider and time and date:
            # Generate a single unique message
            unique_message = generate_single_message(
                patient_name, booked_provider, alternative_provider, time, date
            )

            # Add space before the generated message
            st.write("")  # Empty space for alignment
            
            # Display the generated message in a wider text area
            st.text_area("Generated Message", unique_message, height=200, key="response_message", label_visibility="visible")

        else:
            st.error("Please fill all the fields.")

if __name__ == "__main__":
    main()
