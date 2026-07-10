from fastapi import FastAPI, UploadFile, File
from pypdf import PdfReader
from app.rag.generator import generate_answer
from app.rag.pinecone_db import store_embeddings, search_embeddings
from app.rag.chunking import create_chunks
from fastapi.middleware.cors import CORSMiddleware
from app.rag.embeddings import create_embeddings, create_query_embedding
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Hello from Financial Intelligence Platform!"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    chunks = create_chunks(text)

    embeddings = create_embeddings(chunks)
    store_embeddings(chunks, embeddings)

    return {
    "message": f"{file.filename} uploaded successfully!"
}




@app.post("/ask")
def ask_question(question: str):
    query_embedding = create_query_embedding(question)

    results = search_embeddings(query_embedding)

    context = "\n\n".join(
        [match.metadata["text"] for match in results]
    )

    answer = generate_answer(question, context)

    return {
        "answer": answer
    }