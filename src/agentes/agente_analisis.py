import json
from ..utils import search_file_store

def agente_analisis(client, store_names, extracted_requirements: str, company_profile: dict):
    """
    Agente Analizador: Compara requisitos extraídos con perfil de empresa.
    """
    profile_str = json.dumps(company_profile, indent=2)
    query = f"Compara los requisitos extraídos de la licitación: '{extracted_requirements}' con el perfil de la empresa: '{profile_str}'. Identifica coincidencias, brechas y aspectos de compatibilidad. Responde en español."
    response = search_file_store(query, store_names, client)
    return response.text