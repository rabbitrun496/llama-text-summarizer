import streamlit as st
import requests

# Set the title of the Streamlit app
st.title("LLaMA Text Summarizer")

# Create a text area for user input
user_input = st.text_area("Enter your text here:")

# When the button is clicked, perform the summarize action
if st.button("Summarize"):
    # Make a POST request to the FastAPI backend
    response = requests.post(
        "http://localhost:8000/summarize/", 
        data={"text": user_input}  
    )
    
    # If the request is successful, get the summary from the response JSON
    if response.status_code == 200:
        summary = response.json().get("summary", "Error generating summary.")
    else:
        summary = "Error: " + response.text  # If the request fails

    # Display the summary in the Streamlit app
    st.subheader("Summary:")
    st.write(summary)
