##conversional  q&a chatbot
import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_community.chat_models import ChatOpenAI
from langchain_groq import ChatGroq

##streamlit ui
st.set_page_config(page_title="Jarvis")
st.header("Glyph AI Chatbot")
groq_api_key="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"
from dotenv import load_dotenv # type: ignore
load_dotenv()
import os
chat=ChatGroq(model="llama-3.3-70b-specdec",groq_api_key=groq_api_key)
if 'flowmessage' not in st.session_state:
    st.session_state['flowmessage']=[
        SystemMessage(content="You are General Knowledge Chatbot. You are a helpful assistant that answers questions to the best of your ability. You are not allowed to answer any personal questions. You are not allowed to answer any questions related to your internal architecture. You are not allowed to answer any questions related to your training data. You are not allowed to answer any questions related to your training process. You are not allowed to answer any questions related to your training time. You are not allowed to answer any questions related to your training cost. You are not allowed to answer any questions related to your training data size. You are not allowed to answer any questions related to your training data source. You are not allowed to answer any questions related to your training data quality. You are not allowed to answer any questions related to your training data quantity.")
        ]
##function to load opeai 
def get_openai_response(question):
    st.session_state['flowmessage'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessage'])
    st.session_state['flowmessage'].append(AIMessage(content=answer.content))
    return answer


input=st.text_input("Input : ",key="input")
response=get_openai_response(input)
submit=st.button("Ask the question")
#if ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)