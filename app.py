# Prepare Your CSV Loader
import pandas as pd
df = pd.read_csv("large_employees.csv")
print(df.head())

# Connect LLM (Hugging Face Free Model)
from huggingface_hub import InferenceClient

client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.2")

def ask_llm(user_q, context):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{context}\n\nQuestion: {user_q}"}
    ]
    response = client.chat_completion(messages, max_tokens=300)
    return response.choices[0].message["content"]


# Create CSV → Text Context
context = df.to_string(index=False)[:4000]  # limit to avoid token overflow

# Build Chat UI (Streamlit)
import streamlit as st

st.title("Chat with CSV 🤖")
file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    user_q = st.text_input("Ask a question about the data:")
    if user_q:
        context = df.to_string(index=False)[:4000]
        answer = ask_llm(user_q, context)
        st.write("💡 Answer:", answer)
