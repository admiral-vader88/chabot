import streamlit as st
import google.generativeai as genai

st.markdown("Simple Chat Bot Page By Pranav Jha")
st.sidebar.markdown("Chat bot Page")

Google_api_key = "AIzaSyD_ORntSSSUqszKp1w6aqMuznrWrezDtyk"  # Fixed typo
genai.configure(api_key=Google_api_key)

# Functions to load gemini
geminimodel = genai.GenerativeModel("gemini-pro")
chat = geminimodel.start_chat(history=[])


def get_gemini_response(query):
    """Sends conversation history with message and returns response."""
    instant_response = chat.send_message(query, stream=True)
    return instant_response


st.header("A Simple Chat Bot")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display a single-line text input widget.
input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Get Instant answers")

if submit_button and input_text:
    # Call the get_gemini_response function and get the response
    output = get_gemini_response(input_text)

    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("The Response is")

    # Display the output in the app as Bot response
    for output_chunk in output:
        st.write(output_chunk.text)
        st.session_state['chat_history'].append(("Bot", output_chunk.text))

st.subheader("The Chat History is")

# Show the chat history in the app
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")