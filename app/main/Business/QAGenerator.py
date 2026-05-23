from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from Document import Document
from langfuse.callback import CallbackHandler

class QAGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=self.api_key)
    
    def generate_answer(self, context, question):
        langfuse_handler = self._create_langfuse_handler()
        system_prompt = (
        "You are an assistant for question-answering tasks. "
        "You have access to the following pieces of retrieved context. "
        "Answer **only** from the context provided. "
        "If you don't know the answer based on the context, say 'I don't know'. "
        "Use three sentences maximum and keep the answer concise."
        "\n\n"
        "{context}"
        )
        prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", question),
        ]
        )
    
        context_doc = Document(context, metadata={"some_key": "some_value"})
    
        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)
        return question_answer_chain.invoke({"context": [context_doc], "input": question}, config={"callbacks": [langfuse_handler]})
    