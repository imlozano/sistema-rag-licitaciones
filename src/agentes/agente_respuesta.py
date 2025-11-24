from ..utils import search_file_store

def agente_respuesta(client, store_names, analysis: str):
    """
    Agente Respuesta (Evaluador): Genera puntuación de compatibilidad.
    """
    query = f"Basado en el siguiente análisis: '{analysis}', genera una puntuación de compatibilidad de 0 a 100. Proporciona la puntuación y una breve explicación. Responde en español."
    response = search_file_store(query, store_names, client)
    return response.text