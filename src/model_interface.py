"""
Interface to simulate model inference.
Currently uses a placeholder implementation.
"""
from src.bedrock_client import is_pipeline_ready

def get_response_from_model(query, context):
    #simulate inference for now
    return f"Simulated response for: '{query}'\nContext length: {len(context)}"

def pipeline_status() -> str:
    return "Ready" if is_pipeline_ready() else "Not Initialized"