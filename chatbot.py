import streamlit as st
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
from dotenv import load_dotenv
load_dotenv()
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

# Set page title and favicon
st.set_page_config(page_title="AI Chatbot", page_icon=":robot_face:")

# Sidebar header
with st.sidebar:
    st.title('AI Chatbot')
    st.markdown('''
    **Explore and Learn with AI:**

    - 🤖 Ask questions on various topics.
    - 📚 Receive informative and helpful responses.
    - 💡 Expand your knowledge with AI assistance.

    ''')
    st.info("Note: This chatbot leverages AI to enhance your learning experience.")


st.title("AI Chatbot")
st.subheader("AI Assistance:")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

query = st.text_input("Question: ", key="input")

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()

if query:
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages)  # Use GPT-3.5 Turbo (default model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))

    with st.expander("Show Messages"):
        st.write(messages)
