import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def create_embeddings(chunks):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunks
    )

    return [item.embedding for item in response.data]


def create_query_embedding(query):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )

    return response.data[0].embedding