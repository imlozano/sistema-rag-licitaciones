# Sistema RAG para Compatibilidad de Licitaciones

Este sistema utiliza **Gemini File Search Store** para implementar un sistema RAG (Retrieval Augmented Generation) que evalúa la compatibilidad de empresas con licitaciones.

## ¿Cómo funciona Gemini File Search?

Gemini File Search es un sistema RAG completamente gestionado por Google que permite implementar búsqueda semántica sin necesidad de gestionar infraestructura vectorial. Funciona de la siguiente manera:

### Arquitectura Técnica

1. **File Search Store**: Contenedor para documentos indexados (similar a una base de datos especializada)
2. **Indexación automática**: Al subir documentos, Gemini:
   - Extrae texto (soporta PDF, DOCX, TXT, código, etc.)
   - Aplica chunking inteligente automático
   - Genera embeddings de última generación
   - Almacena chunks en la infraestructura de Google
3. **Búsqueda semántica**: Las consultas se convierten en embeddings y se buscan chunks similares usando similitud del coseno
4. **Generación fundamentada**: Los chunks relevantes se inyectan en el contexto del modelo Gemini para generar respuestas

### Ventajas

- ✅ **Sin infraestructura**: No necesitas Pinecone, Chroma, ni gestionar bases vectoriales
- ✅ **Indexación automática**: Chunking inteligente y embeddings incluidos
- ✅ **Búsqueda semántica**: Entiende significado, no solo palabras clave
- ✅ **Citaciones automáticas**: Verificabilidad de fuentes
- ✅ **Escalabilidad**: Gestionado por Google

### Precios

- **Storage**: GRATIS ✨
- **Embeddings en indexación**: $0.15 por 1M tokens (una sola vez)
- **Embeddings en búsqueda**: GRATIS
- **Tokens recuperados**: Se cobran como context tokens del modelo

## Características del Sistema

- **Subida de PDFs**: Sube múltiples documentos de licitaciones a Gemini File Search Store
- **Extracción automática**: Extrae requisitos clave de los documentos usando consultas RAG
- **Análisis de compatibilidad**: Compara con el perfil de la empresa usando búsqueda semántica
- **Puntuación**: Genera una score de compatibilidad del 0-100
- **Interfaz web**: UI en Streamlit para fácil uso

## Arquitectura Implementada

### Componentes Mínimos (según especificaciones)

1. **Fuente de datos**: Documentos PDF de licitaciones (máx. 20 archivos)
2. **Extracción**: Lectura directa de texto de PDFs usando Gemini File Search
3. **Segmentación (chunks)**: Chunking automático inteligente manejado por File Search Store
4. **Embeddings y similitud**: Gemini maneja embeddings y búsqueda semántica (similitud del coseno)
5. **Base de datos vectorial**: File Search Store (gestionado por Google, no requiere FAISS/Pinecone/etc.)
6. **Arquitectura multiagente**: 3 agentes LangChain (Extractor, Analizador, Evaluador)
7. **Interfaz**: Streamlit para subir archivos y ver resultados
8. **Repositorio**: Este repo con código funcional

## Instalación

1. Clona el repositorio
2. Instala dependencias: `pip install -r requirements.txt`
3. Ejecuta: `streamlit run src/app.py`
   - Si hay problemas de importación, usa: `PYTHONPATH=. streamlit run src/app.py`

## Uso

1. Ingresa tu API Key de Google AI Studio
2. Sube uno o más PDFs de licitaciones
3. Ingresa el perfil de empresa en formato JSON
4. Haz clic en "Analizar"
5. Revisa los resultados: requisitos extraídos, análisis y puntuación

## Tecnologías

- Python
- Google Gemini File Search (google-genai)
- LangChain (para arquitectura multiagente)
- Streamlit (interfaz web)

## Referencia

Implementación basada en el tutorial oficial: [Gemini File Search Tutorial](https://colab.research.google.com/github/alarcon7a/youtube-tutorial-sources/blob/main/Notebooks/Google%20AI/Gemini/Tools/gemini_file_search_tutorial.ipynb)

El sistema sigue exactamente las mejores prácticas del tutorial, incluyendo:
- Uso de `google.genai` para File Search Store
- Indexación automática con chunking inteligente
- Búsqueda semántica con citaciones
- Arquitectura RAG sin gestión de vectores manual

## Para mas informacion

- [Documentación de Google AI](https://ai.google.dev/)
- [Repositorio de LangChain](https://github.com/langchain-ai/langchain)
- [Gemini File Search Documentación](https://blog.google/technology/developers/file-search-gemini-api/)

## Para datos de prueba

Los datos se pueden descargar a traves de la [SECOPII](https://www.colombiacompra.gov.co/secop/secop-ii/consulte-en-el-secop-ii)

1. Procesos de Contratación de las Entidades Estatales registradas
2. Tipo de proceso
3. Licitación pública


 
