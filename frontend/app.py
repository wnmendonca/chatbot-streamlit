import streamlit as st
import requests
import json
import warnings
from uuid import uuid4

# Configurações globais
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Funções de cache
@st.cache_data
def get_prompts():
    return []

@st.cache_data
def get_querys():
    return []

@st.cache_data
def get_session_id():
    return str(uuid4())

global prompts,querys,session_id

prompts = get_prompts()
querys = get_querys()
session_id = get_session_id()
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid4())

# Função para exibir mensagens no chat
def chat():
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Olá! Como posso te ajudar?"}]

    for msg in st.session_state.messages:
        if msg["role"] == "assistant":
            st.chat_message(msg["role"]).write(msg["content"])
        else:
            st.chat_message(msg["role"]).write(msg["content"])

    messages = []
    
    if prompt := st.chat_input():
        data = {
        'input_string': prompt,
        'session_id':st.session_state.session_id,
        'messages': st.session_state["messages"]
        }
        
        st.chat_message("user").write(prompt)
        st.session_state["messages"].append({"role": "user", "content": prompt})
        response = requests.post(f"http://localhost:8000/chat/",json=data)
        msg = json.loads(response.content.decode('utf-8')).get("answer")
        query = json.loads(response.content.decode('utf-8')).get("query")
        if msg:
            messages.append({"role": "assistant", "content": msg, "likes": 0})
            st.chat_message("assistant").write(msg)
            st.session_state["messages"].append({"role": "assistant", "content": msg})
            prompts.append(prompt)
            querys.append(query)

def main():
    st.title("💬 Chatbot")
    global prompts,querys,session_id
    chat()

if __name__ == "__main__":
    user_data = {}
    prompts = get_prompts()
    querys = get_querys()
    session_id = get_session_id()
    main()
