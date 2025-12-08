from pydantic_ai import Agent
from backend.data_models import RagResponse
from backend.constants import VECTOR_DATABASE_PATH
import lancedb

vector_db = lancedb.connect(uri=VECTOR_DATABASE_PATH)

rag_agent = Agent(model="google-gla:gemini-2.5-flash", retries=2, system_prompt=(
        "You are a teacher and youber with a burning passion for data engineering, teaching in videos and i person",
        "You are friendly, helpful with a vast knowledge and a love for bunnies",
        "Always answer based on the retrieved knowledge, but you can fill in if you feel it's really needed",
        "Don't hallucinate, rather say you can't answer it if the user prompts outside of the retrieved knowledge or give a 2 sentence fact about bunnies",
        "Make sure you give a clear and short answer unless requested to elaborate on it",
        "Also describe which video the information came from",
    ),
    output_type=RagResponse
)

@rag_agent.tool_plain
def retrieve_top_documents(query: str, k=3) -> str:
    """
    Uses vector search to find the closest k matchin documents to the query
    """
    results = vector_db["videoTranscripts"].search(query=query).limit(k).to_list()
    top_result = results[0]
    return f"""
    Filename: {top_result["filename"]},

    Filepath: {top_result["filepath"]},

    Content: {top_result["content"]}
    """