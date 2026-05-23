from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class PDFDocumentProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.docs = None

    def load_and_split(self):
        loader = PyPDFLoader(self.file_path)
        self.docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        return text_splitter.split_documents(self.docs)