import streamlit as st
import getpass
import os
import bs4
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# import dotenv

# dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = getpass.getpass()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()


st.write("Hello world")

st.write("this is the second one ")


st.title("My first app")
'''
1. Pull in QA from Langchain 
2. Input for doc to QA
3. How will we be interacting with doc
4. Output of QA 

'''

