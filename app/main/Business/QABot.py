from PDFDocumentProcessor import PDFDocumentProcessor
from RetrievalSystem import RetrievalSystem
from QAGenerator import QAGenerator

class QABot:
    def __init__(self, file_path, api_key):
        self.pdf_processor = PDFDocumentProcessor(file_path)
        self.api_key = api_key
        self.retrieval_system = None
        self.qa_generator = None

    def setup(self):
        splits = self.pdf_processor.load_and_split()
        if self.retrieval_system is None:
            self.retrieval_system = RetrievalSystem(splits, self.api_key)
        else:
            self.retrieval_system.documents += splits
            
        self.retrieval_system.load_vector_store()

        self.qa_generator = QAGenerator(self.api_key)

    def run_query(self, query):
        self.setup()
        docs = self.retrieval_system.retrieve(query)
        context = " ".join(doc.page_content[:300] for doc in docs)  
        response = self.qa_generator.generate_answer(context, query)
        return response
    
    def createvector_store(self):
        if self.retrieval_system is not None:
            self.retrieval_system.create_vector_store()
        else:
            raise ValueError("Retrieval system is not initialized.")
