import streamlit as st
from api_utils import upload_document, list_documents, delete_document

def display_sidebar():
    st.sidebar.text(f"Session ID: {st.session_state.session_id}")
    model_options = ["mistral:7b"]
    st.sidebar.selectbox("Select Model", options=model_options, key="model")

    st.sidebar.header("Upload Document")
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "txt", "docx"])
    if uploaded_file is not None:
        if st.sidebar.button("Upload"):
            with st.spinner("Uploading and processing the document..."):
                # Call your function to process the uploaded file
                upload_response = upload_document(uploaded_file)
                st.sidebar.success(f"File Uploaded and processed successfully! with the id {upload_response['file_id']}")
                st.session_state.documents = list_documents()

    st.sidebar.header("Uploaded Documents")
    if st.sidebar.button("Refresh Document List"):
        with st.spinner("Refreshing..."):
            st.session_state.documents = list_documents()

    if "documents" in st.session_state and st.session_state.documents:
        for doc in st.session_state.documents:
            st.sidebar.text(f"{doc['filename']} (ID: {doc['id']})")

        selected_doc_id = st.sidebar.selectbox(f"Select Document to Delete (ID: {doc['id']})", 
                                                   options=[doc['id'] for doc in st.session_state.documents])
        if st.sidebar.button("Delete selected document"):
            with st.spinner("Deleting document..."):
                delete_response = delete_document(selected_doc_id)
                if delete_response:
                    st.sidebar.success(f"Document ID {selected_doc_id} deleted successfully!")
                    st.session_state.documents = list_documents()
                else:
                    st.sidebar.error(f"Failed to delete Document ID {selected_doc_id}.")
    

