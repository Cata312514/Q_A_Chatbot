# Import required libraries
import os
from dotenv import load_dotenv
import openai
from PyPDF2 import PdfReader
#from langchain.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
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

# Retrieves your pdf documents.
def ingest_docs(pdf_files):
    text = ""
    for pdf in pdf_files:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

     
# split texts into chunks
def split_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = text_splitter.split_text(text)
    return chunks


# create embeddings using langchain's openai embeddings wrapper
# Then store to Pinecon
def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    #embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = Pinecone.from_texts(texts=text_chunks, embedding=embeddings, index_name=index_name)
    return vectorstore
    
    
if __name__ == '__main__':
    ingest_docs()