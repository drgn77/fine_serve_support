from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, os.getenv("DATA_PATH", "data"))
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
VECTOR_PATH = os.path.join(BASE_DIR, "vector_data")


loader = DirectoryLoader(path=DATA_PATH, glob="**/*.md", loader_cls=TextLoader, loader_kwargs={"encoding": "utf-8"})
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = text_splitter.split_documents(docs)
print(f"Loaded {len(docs)} documents")
print(f"Split into {len(chunks)} chunks")
embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
vector_store = FAISS.from_documents(chunks, embeddings)
vector_store.save_local(VECTOR_PATH)

