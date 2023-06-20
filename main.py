# Import required libraries
import streamlit as st
from streamlit_chat import message
from typing import Set
from ingestion import ingest_docs, split_text_chunks, get_vectorstore
from core import run_llm
from htmlTemplates import user_template, bot_template, css

# Retrieves answer to question from the database and store all questions and answers
def control_userinput(user_query):
    response = st.session_state.conversation({'question': user_query})
    st.session_state.chat_history = response['chat_history']
    
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
            
# Setting up Streamlit interface            
def main():
    st.set_page_config(page_title="Smart PDF Chatbot", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    
    # Creates an empty list that will store all the user prompts
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    # Creates an empty list that will store all the chatbot answers
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header("Smart PDF Chatbot :books:")
    
    # Variable for user question
    user_query = st.text_input("Ask anything about the documents: ")
    
    # Retrieves answer to question from the database and store all questions and answers
    if user_query:
        st.spinner("Generating response...")
        control_userinput(user_query)
            
            
    with st.sidebar:
        st.subheader("Documents")
        pdf_files = st.file_uploader("Uplod your PDF files here and press Upload", accept_multiple_files=True)
        if st.button("Upload"):
            with st.spinner("Uploding files..."):
                # retrieve pdf text
                raw_text = ingest_docs(pdf_files)
                # get text chunks
                text_chunks = split_text_chunks(raw_text)
                # create vector embeddings
                vectorstore = get_vectorstore(text_chunks)
                #Create conversation chain
                st.session_state.conversation = run_llm(vectorstore)


if __name__ == '__main__':
    main()


