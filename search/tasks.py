# from celery import shared_task
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_core.documents import Document as LangDoc
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS
# import os

# @shared_task
# def index_document_task(text, title):
#     splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
#     chunks = splitter.split_text(text)
#     docs = [LangDoc(page_content=chunk, metadata={"source": title}) for chunk in chunks]
#     embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

#     if not os.path.exists("faiss_index"):
#         vectorstore = FAISS.from_documents(docs, embeddings)
#     else:
#         vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
#         vectorstore.add_documents(docs)

#     vectorstore.save_local("faiss_index")

import os
from celery import shared_task
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document as LangDoc
from langchain_community.embeddings import HuggingFaceEmbeddings

@shared_task
def index_document_task(text, title):
    try:
        print(f"[*] Starting indexing for: {title}")
        
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_text(text)
        docs = [LangDoc(page_content=chunk, metadata={"source": title}) for chunk in chunks]

        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        index_path = os.path.join(os.getcwd(), "faiss_index")

        if not os.path.exists(index_path):
            print("[+] Creating new FAISS index")
            vectorstore = FAISS.from_documents(docs, embeddings)
        else:
            print("[+] Loading existing FAISS index")
            vectorstore = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
            vectorstore.add_documents(docs)

        vectorstore.save_local(index_path)
        print(f"[✓] Finished indexing for: {title}")
        
    except Exception as e:
        print(f"[x] Error in index_document_task: {str(e)}")
