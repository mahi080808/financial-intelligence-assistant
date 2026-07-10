import os
from dotenv import load_dotenv
from pinecone import Pinecone
load_dotenv()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("financial-intelligence")


def store_embeddings(chunks, embeddings):
    vectors = []

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        vectors.append({
            "id": str(i),
            "values": embedding,
            "metadata": {
                "text": chunk
            }
        })

    index.upsert(vectors=vectors)
def search_embeddings(query_embedding):
    results = index.query(
        vector=query_embedding,
        top_k=3,
        include_metadata=True
    )

    return results.matches