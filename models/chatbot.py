import os
from embedding import download_hugging_face_embeddings
from pinecone_setup import initialize_pinecone
from pdf_loader import load_pdf, text_split
from appointment import book_appointment
from google_maps import get_nearby_hospitals
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import CTransformers
from transformers import AutoModel
import datetime

class Chatbot:
    def __init__(self):
        self.docsearch = initialize_pinecone()
        self.qa_chain = self.create_qa_chain()
        self.user_location = None  
    
    def create_qa_chain(self):
        prompt_template = """
        Use the following pieces of information to answer the user's question.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        Context: {context}
        Question: {question}

        Only return the helpful answer below and nothing else.
        Helpful answer:
        """
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        
        llm = self.load_model()
        qa = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.docsearch.as_retriever(search_kwargs={'k': 2}),
            return_source_documents=True,
            chain_type_kwargs={"prompt": PROMPT}
        )
        return qa

    def load_model(self):
        model = AutoModel.from_pretrained("TheBloke/Llama-2-7B-Chat-GGML")
        llm = CTransformers(model="/model/Llama-2-7B-Chat-GGML/llama-2-7b-chat.ggmlv3.q4_K_M.bin", model_type="llama",
                            config={'max_new_tokens': 512, 'temperature': 0.8})
        return llm
    def set_user_location(self, location):
        self.user_location = location

    def handle_input(self, user_input):
        if self.user_location and "emergency" in user_input.lower():
            hospitals = get_nearby_hospitals(self.user_location)
            if hospitals:
                hospital_names = [hospital["name"] for hospital in hospitals]
                return f"Here are some nearby hospitals: {', '.join(hospital_names)}"
            else:
                return "I'm sorry, but I couldn't find any nearby hospitals."
        elif "schedule appointment" in user_input.lower():
            # still working on it
            doctor_name = "" 
            appointment_time = datetime.datetime.now() + datetime.timedelta(days=1)  # Example: schedule for tomorrow
            return book_appointment(doctor_name, appointment_time)
        else:
            result = self.qa_chain({"query": user_input})
            return result['result']
    