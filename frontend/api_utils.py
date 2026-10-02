import requests
import streamlit as st
import os
from dotenv import load_dotenv

if not os.getenv("BACKEND_URL"):
    print("Loading .env")
    load_dotenv()

api_base_url = os.getenv("BACKEND_URL")

def get_api_response(question, session_id, model):

    api_url = f"{api_base_url}/chat"
    payload = {
        "question": question,
        "model": model
    }

    if session_id:
        payload["session_id"] = session_id

    response = requests.post(api_url, json=payload, headers={"Content-Type": "application/json"})
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

def upload_document(file):
    api_url = f"{api_base_url}/upload-doc"
    files = {"file": (file.name, file, file.type)}
    
    response = requests.post(api_url, files=files)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None
    
def list_documents():
    api_url = f"{api_base_url}/list-docs"
    response = requests.get(api_url)
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

def delete_document(file_id):
    api_url = f"{api_base_url}/delete-doc"
    payload = {"file_id": file_id}
    
    response = requests.post(api_url, json=payload, headers={"Content-Type": "application/json"})
    
    try:
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None