import streamlit as st
import google.generativeai as genai

st.markdown("Simple Chat Bot Page By Pranav Jha")
st.sidebar.markdown("Chat bot Page")

Google_api_key = ""
genai.configure(api_key=Google_api_key)


geminimodel = genai.GenerativeModel("gemini-pro")
chat = geminimodel.start_chat(history=[])


def get_gemini_response(query):
    """Sends conversation history with message and returns response."""
    instant_response = chat.send_message(query, stream=True)
    return instant_response


st.header("A Simple Chat Bot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Get Instant answers")

if submit_button and input_text:
    output = get_gemini_response(input_text)
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("The Response is")

   
    for output_chunk in output:
        st.write(output_chunk.text)
        st.session_state['chat_history'].append(("Bot", output_chunk.text))

st.subheader("The Chat History is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
