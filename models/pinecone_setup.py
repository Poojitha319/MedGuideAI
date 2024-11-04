import os
import pinecone
from langchain.vectorstores import Pinecone as PineconeStore
from embedding import download_hugging_face_embeddings

def initialize_pinecone():
    pinecone.init(api_key=os.environ["PINECONE_API_KEY"], environment=os.environ["PINECONE_API_ENV"])
    index_name = "medguide"
    if index_name not in pinecone.list_indexes():
        pinecone.create_index(name=index_name, dimension=384, metric="cosine")
    return PineconeStore.from_existing_index(index_name, download_hugging_face_embeddings())
