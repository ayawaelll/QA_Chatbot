from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
import os

class RetrievalSystem:
    def __init__(self, documents, api_key):
        self.documents = documents
        self.api_key = api_key
        self.retriever = None
    
    def create_vector_store(self):
        embeddings = OpenAIEmbeddings(api_key=self.api_key)
        self.retriever = FAISS.from_documents(self.documents, embeddings)
        self.retriever.save_local("embedded_file_faiss")
    
    def load_vector_store(self):
        embeddings = OpenAIEmbeddings(api_key=self.api_key)
        if os.path.exists("embedded_file_faiss"):
            self.retriever = FAISS.load_local("embedded_file_faiss", embeddings, allow_dangerous_deserialization=True)
            temp_retriever = FAISS.from_documents(self.documents, embeddings)
            self.retriever.merge_from(temp_retriever)
            self.retriever.save_local("embedded_file_faiss")
        else:
            raise ValueError("Vector store does not exist. Create it first using create_vector_store.")

    def retrieve(self, query, k=2):
        if self.retriever is None:
            raise ValueError("Retriever has not been initialized.")
        return self.retriever.similarity_search(query, k=k)
