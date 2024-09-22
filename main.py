import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from api import Groq_API, Mistral_API
from langchain_mistralai import MistralAIEmbeddings
import streamlit as st
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from streamlit_chat import message
os.environ["GROQ_API_KEY"]=Groq_API
os.environ["MISTRALAI_API_KEY"] = Mistral_API
llm = ChatGroq(model="llama3-8b-8192")
if 'responses' not in st.session_state:
    st.session_state['responses'] = ["Welcome to Apple, How can I assist you?"]
if 'requests' not in st.session_state:
    st.session_state['requests'] = []
if 'buffer_memory' not in st.session_state:
            st.session_state.buffer_memory=ConversationBufferWindowMemory(k=3,return_messages=True)
if "vector" not in st.session_state:
    st.session_state.embedding =  MistralAIEmbeddings(model="mistral-embed", api_key=Mistral_API)
    st.session_state.documents = []
    #st.session_state.urls = ["https://www.apple.com/","https://www.apple.com/store","https://www.apple.com/iphone","https://www.apple.com/ipad","https://www.apple.com/mac","https://www.apple.com/apple-vision-pro/","https://www.apple.com/airpods/","https://www.apple.com/tv-home/","https://www.apple.com/services/","https://www.apple.com/shop/accessories/all"]
    #for url in st.session_state.urls:
    st.session_state.loader = WebBaseLoader("https://www.apple.com/")
    st.session_state.docs = st.session_state.loader.load()
    #st.session_state.documents.extend(st.session_state.docs)
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    st.session_state.doc = st.session_state.text_splitter.split_documents(st.session_state.docs)
    st.session_state.db = FAISS.from_documents(documents = st.session_state.doc, embedding=st.session_state.embedding)
prompt = ChatPromptTemplate.from_template("""Suggest user a product along with its description and features according to their requirement along with URL to view that product, URL should be from context and working. Also, solve FAQs of customers.
<context>
{context}
</context>
Question: {input}""")
document_chain = create_stuff_documents_chain(llm,prompt)
retriever = st.session_state.db.as_retriever()
retrieval_chain = create_retrieval_chain(retriever,document_chain)
st.title("Apple Chatbot")
...
response_container = st.container()
textcontainer = st.container()
...
with textcontainer:
    query = st.text_input("Query: ")
    if query:
        with st.spinner("typing..."):
            response = retrieval_chain.invoke({"input":query})
        st.session_state.requests.append(query)
        st.session_state.responses.append(response['answer'])
with response_container:
    if st.session_state['responses']:
        for i in range(len(st.session_state['responses'])):
            message(st.session_state['responses'][i],key=str(i))
            if i < len(st.session_state['requests']):
                message(st.session_state["requests"][i], is_user=True,key=str(i)+ '_user')
