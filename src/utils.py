from google import genai
from google.genai import types
import time
import os

def create_file_search_store(display_name: str, api_key: str):
    """
    Create a new File Search Store.
    """
    client = genai.Client(api_key=api_key)
    store = client.file_search_stores.create(config={'display_name': display_name})
    return store, client

def upload_file_to_store(file_path: str, store_name: str, client: genai.Client, display_name: str = None, custom_metadata: list = None):
    """
    Upload and index a file to the File Search Store.
    """
    config = {}
    if display_name:
        config['display_name'] = display_name
    if custom_metadata:
        config['custom_metadata'] = custom_metadata

    operation = client.file_search_stores.upload_to_file_search_store(
        file=file_path,
        file_search_store_name=store_name,
        config=config if config else None
    )

    # Wait for indexing
    while not operation.done:
        time.sleep(5)
        operation = client.operations.get(operation)

    return True

def search_file_store(query: str, store_names: list, client: genai.Client, model: str = 'gemini-2.5-flash', metadata_filter: str = None):
    """
    Search the File Search Store.
    """
    file_search_config = types.FileSearch(file_search_store_names=store_names)
    if metadata_filter:
        file_search_config.metadata_filter = metadata_filter

    response = client.models.generate_content(
        model=model,
        contents=query,
        config=types.GenerateContentConfig(
            tools=[types.Tool(file_search=file_search_config)]
        )
    )
    return response