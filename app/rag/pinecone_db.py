import os
from dotenv import load_dotenv
from pinecone import Pinecone

# Load environment variables
load_dotenv()


def get_index():
    """
    Creates a Pinecone client and returns the index.
    This avoids creating the client during application startup.
    """
    pc = Pinecone(
        api_key=os.getenv("PINECONE_API_KEY")
    )

    return pc.Index("financial-intelligence")


def store_embeddings(chunks, embeddings):
    index = get_index()

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
    index = get_index()

    results = index.query(
        vector=query_embedding,
        top_k=3,
        include_metadata=True
    )

    return results.matches