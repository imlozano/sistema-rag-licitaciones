import streamlit as st
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import create_file_search_store, upload_file_to_store
from src.agentes.agente_extraccion import agente_extraccion
from src.agentes.agente_analisis import agente_analisis
from src.agentes.agente_respuesta import agente_respuesta

st.title("Sistema RAG para Compatibilidad de Licitaciones")

api_key = st.text_input("Clave API de Google", type="password")

pdf_files = st.file_uploader("Subir PDFs de Licitaciones", type="pdf", accept_multiple_files=True)

company_profile_json = st.text_area("Perfil de Empresa (JSON)", placeholder='{"experiencia": "5 años", "capacidades": ["construcción", "ingeniería"]}')

if st.button("Analizar"):
    if not api_key or not pdf_files or not company_profile_json:
        st.error("Por favor, proporciona todos los inputs.")
    else:
        try:
            company_profile = json.loads(company_profile_json)
            # Crear store
            store, client = create_file_search_store("Licitaciones Store", api_key)
            st.info(f"Store creado: {store.display_name}")

            # Subir archivos
            for pdf_file in pdf_files:
                temp_path = f"temp_{pdf_file.name}"
                with open(temp_path, "wb") as f:
                    f.write(pdf_file.getvalue())
                upload_file_to_store(temp_path, store.name, client, display_name=pdf_file.name)
                os.remove(temp_path)
                st.info(f"Archivo subido: {pdf_file.name}")

            # Ejecutar agentes
            extracted = agente_extraccion(client, [store.name])
            st.subheader("Requisitos Extraídos")
            st.write(extracted)

            analysis = agente_analisis(client, [store.name], extracted, company_profile)
            st.subheader("Análisis de Compatibilidad")
            st.write(analysis)

            score = agente_respuesta(client, [store.name], analysis)
            st.subheader("Puntuación de Compatibilidad")
            st.write(score)

        except json.JSONDecodeError:
            st.error("El JSON del perfil de empresa no es válido.")
        except Exception as e:
            st.error(f"Error: {str(e)}")