# Chatbot-GroqAI
This chatbot interacts with LLM (GroqAI) via langchain to provide questions asked by the chatbot. The chatbot uses streamlit to work on frontend.

# Groq AI Chatbot Web App

This project is a **conversational AI chatbot web app** built using [Streamlit](https://streamlit.io/) and [LangChain](https://www.langchain.com/) with a Groq LLM backend (Llama 3). The app supports **live streaming responses** and retains conversation history for context-aware answers.

## Features

- Conversational interface with memory (shows previous dialog)
- Uses Groq's Llama-3.3-70b model via LangChain
- Streams answers in real time for enhanced user experience
- Easy customization for prompt and model parameters

## Setup

### Prerequisites

- Python 3.8+
- Required API Keys:
  - **GROQ_API_KEY:** Your Groq API key
  - **LANGCHAIN_API_KEY:** Your LangChain API key
- [Streamlit](https://streamlit.io/)
- [langchain_groq](https://python.langchain.com/groq)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

### Installation

1. **Clone the repository**  

git clone [https://github.com/vedant2606/your-repo.git](https://github.com/Vedant2606/Chatbot-GroqAI.git)
cd your-repo


2. **Install dependencies:**  
pip install -r requirements.txt


3. **Set up your `.env` file**  
Create a `.env` file in the project root with:
GROQ_API_KEY=your-groq-api-key
LANGCHAIN_API_KEY=your-langchain-api-key
LANGCHAIN_PROJECT=true


## Usage

1. **Start the app**
streamlit run app.py


2. **Access in browser**  
Go to `http://localhost:8501` to use your chatbot.

## File Structure

- `app.py`: Main application script
- `.env`: Environment variables
- `requirements.txt`: Python dependencies

## Customization

- Edit model parameters (`temperature`, `top_p`, etc.) in `app.py`.
- Adjust prompt template for different assistant behaviors.
