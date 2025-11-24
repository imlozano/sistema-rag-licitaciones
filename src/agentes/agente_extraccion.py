from ..utils import search_file_store

def agente_extraccion(client, store_names):
    """
    Agente Extractor: Extrae requisitos clave de los documentos de licitación subidos.
    """
    query = "Extrae todos los requisitos clave, especificaciones y criterios de los documentos de licitación subidos. Lista ellos en un formato estructurado. Responde en español."
    response = search_file_store(query, store_names, client)
    return response.text