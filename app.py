import streamlit as st
from agent import Agent
import nltk
nltk.download('punkt')



def process_input(text):
    tokens = nltk.word_tokenize(text)
    return tokens
st.title('AI Agent Interaction')

# User inputs for agent details
name = st.text_input("Enter the agent's name")
role = st.text_input("Enter the agent's role")

if st.button("Create Agent"):
    agent = Agent.create_agent(name, role)
    st.write("Agent created successfully")
    st.write(f"Name: {agent.name}")
    st.write(f"Role: {agent.role}")

if st.button("List Agents"):
    st.write("Existing Agents:")
    for agent in Agent.agents:
        st.write(f"Name: {agent.name}, Role: {agent.role}")
        
# NLP processing demonstration
st.subheader("NLP Processing")
user_input = st.text_area("Enter text for NLP processing")

if st.button("Process Text"):
    tokens = process_input(user_input)
    st.write("Tokenized Text:", tokens)

