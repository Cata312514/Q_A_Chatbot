# Import required libraries
import os
from dotenv import load_dotenv
import openai
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Pinecone
import pinecone


# Load environment variable from .env file
load_dotenv()
    
# Access environment variables
openai.api_key = os.getenv('OPEN_API_KEY')
pinecone.init(api_key=os.environ['PINECONE_API_KEY'],
              environment=os.environ['PINECONE_ENVIRONEMENT_REGION'])

# Accessing Pinecone index
index_name = "chatbot-app"

# Implementing the llm chain and retrieves data from Pinecone vectorstore
def run_llm(vectorstore):
    llm = ChatOpenAI(verbose=True, temperature=0)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
        )
    return conversation_chain


if __name__ == "__main___":
    run_llm()
    