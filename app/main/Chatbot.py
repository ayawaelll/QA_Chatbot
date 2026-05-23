import streamlit as st
import sys
sys.path.append('Business')
from QABot import QABot
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

# Main title and description
st.title("💬 PDF Q&A Chatbot")
st.caption("🚀 A Streamlit chatbot powered by your custom PDF processing and OpenAI")

# Check if the chat session state is initialized
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Display previous chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

file_path = "C:/Users/PCAdmin/source/repos/QA_Chatbot_PDF/Data/lecture-9-Memory.pdf"
bot = QABot(file_path, openai_api_key)


# Handle new user input
if prompt := st.chat_input():
    # Save user message and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Run the query using your chatbot
    response = bot.run_query(prompt)
    
    # Save and display the assistant's response
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

