from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT'] = 'true'


if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
st.title("Chatbot with GroqAI")
for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

# Input field
input_text = st.chat_input("Write your query here.")

# Define the LLM model
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    streaming=True,
    model_kwargs={"top_p": 0.9, "frequency_penalty": 0.2}
)

output_parser = StrOutputParser()

# Define the prompt template with conversation history
def get_chat_prompt():
    chat_history = "\n".join(
        [f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.messages[-5:]]  # Use last 5 messages
    )
    return ChatPromptTemplate.from_messages([
        ("system", f"You are a helpful assistant. Use the conversation history to generate better responses. \n\nChat History:\n{chat_history}"),
        ("user", "Question: {question}")
    ])

# Function to stream response
def stream_response(input_text):
    chat_prompt = get_chat_prompt()
    formatted_prompt = chat_prompt.format(question=input_text)  
    chain = llm | output_parser  
    response_stream = chain.stream(formatted_prompt)  

    for chunk in response_stream:
        yield chunk 

# Process input when user submits a query
if input_text:
    st.chat_message("user").markdown(input_text)
    st.session_state.messages.append({"role": "user", "content": input_text})

    with st.chat_message("assistant"):
        response_text = st.write_stream(stream_response(input_text))

    
    st.session_state.messages.append({"role": "assistant", "content": response_text})
