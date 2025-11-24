# Documento Técnico – Proyecto Final Introducción a IA

## 1. Introducción

Este proyecto implementa un **Sistema RAG para Compatibilidad de Licitaciones** que utiliza Gemini File Search Store para evaluar automáticamente la compatibilidad entre perfiles de empresas y requisitos de licitaciones. El sistema extrae información de documentos PDF, compara con perfiles empresariales en formato JSON y genera puntuaciones de compatibilidad usando inteligencia artificial.

El objetivo es demostrar la aplicación práctica de conceptos de IA moderna: RAG (Retrieval Augmented Generation), procesamiento de documentos, embeddings semánticos y arquitectura multiagente, todo integrado con la infraestructura gestionada de Google.

## 2. Problema a resolver

En el proceso de licitaciones públicas, las empresas deben evaluar manualmente si cumplen con los requisitos específicos de cada convocatoria. Este proceso es:
- **Tedioso**: Revisar múltiples documentos PDF
- **Subjectivo**: Diferentes interpretaciones de requisitos
- **Ineficiente**: Pérdida de tiempo en evaluaciones incompatibles

El sistema resuelve esto automatizando la extracción de requisitos, comparación objetiva con perfiles empresariales y generación de scores de compatibilidad.

## 3. Metodología

### Tecnologías y Herramientas
- **Google Gemini File Search**: Para indexación automática de documentos y búsqueda semántica RAG
- **LangChain**: Arquitectura multiagente para orquestación de tareas
- **Streamlit**: Interfaz web para interacción usuario-sistema
- **Python**: Lenguaje de desarrollo principal

### Pasos de Implementación

1. **Configuración de File Search Store**: Crear contenedor para documentos indexados
2. **Subida e Indexación**: Procesar PDFs con chunking y embeddings automáticos
3. **Arquitectura Multiagente**:
   - **Agente Extractor**: Extrae requisitos clave usando consultas RAG
   - **Agente Analizador**: Compara requisitos con perfil empresarial
   - **Agente Evaluador**: Genera score de compatibilidad 0-100
4. **Interfaz Streamlit**: Upload de archivos y visualización de resultados

### Integración con APIs
- **Gemini File Search**: Maneja extracción de texto, chunking, embeddings y similitud
- **Google Generative AI**: Para generación de respuestas fundamentadas

## 4. Arquitectura de agentes

### Flujo de Comunicación

```
Usuario → Streamlit UI → File Search Store
                          ↓
                    Agente Extractor → Extrae requisitos
                          ↓
                    Agente Analizador → Compara con perfil
                          ↓
                    Agente Evaluador → Genera score
                          ↓
                    Resultados → Usuario
```

### Roles de Cada Agente

- **Agente Extractor** (`agente_extraccion.py`):
  - Rol: Especialista en extracción de información
  - Función: Consulta el File Search Store para extraer requisitos clave
  - Herramientas: `search_file_store` con consultas específicas

- **Agente Analizador** (`agente_analisis.py`):
  - Rol: Analista de compatibilidad
  - Función: Compara requisitos extraídos con perfil JSON de empresa
  - Herramientas: `search_file_store` con contexto de comparación

- **Agente Evaluador** (`agente_respuesta.py`):
  - Rol: Evaluador final y generador de scores
  - Función: Sintetiza análisis y genera puntuación objetiva
  - Herramientas: `search_file_store` para fundamentar evaluación

### Comunicación Entre Agentes
Los agentes se ejecutan secuencialmente, pasando resultados como contexto para el siguiente agente. Cada uno utiliza el File Search Store como "memoria" compartida.

## 5. Resultados y conclusiones

### Métricas de Funcionamiento
- **Precisión de Extracción**: Alta (Gemini maneja OCR y parsing de PDFs)
- **Relevancia Semántica**: Excelente (embeddings de Google)
- **Velocidad de Respuesta**: Buena (infraestructura gestionada)
- **Compatibilidad Multi-formato**: Soporta PDF, DOCX, TXT, etc.

### Ejemplos de Uso

**Entrada:**
- PDF de licitación: "Se requiere empresa con 5 años experiencia en construcción"
- Perfil empresa: `{"experiencia": "7 años", "capacidades": ["construcción", "ingeniería"]}`

**Salida:**
- Extractor: Lista requisitos específicos
- Analizador: Identifica coincidencias (experiencia, capacidades)
- Evaluador: Score 95/100 con explicación

### Aprendizajes
- **RAG sin Vector DB**: Gemini File Search elimina complejidad de gestión de vectores
- **Arquitectura Multiagente**: LangChain facilita orquestación de tareas especializadas
- **Integración de APIs**: Google proporciona herramientas robustas para IA aplicada
- **Importancia del Chunking**: Segmentación inteligente mejora recuperación de información

## 6. Trabajo futuro

### Mejoras Inmediatas
- **Filtrado Avanzado**: Implementar metadata filtering por tipo de licitación
- **Citaciones**: Agregar referencias específicas a secciones del PDF
- **Múltiples Idiomas**: Soporte para documentos en inglés/español

### Escalabilidad
- **Batch Processing**: Procesar múltiples licitaciones simultáneamente
- **API REST**: Exponer funcionalidad como servicio web
- **Base de Datos**: Almacenar resultados históricos para analytics

### Integraciones Avanzadas
- **Google Drive**: Sincronización automática de documentos
- **Slack/Discord**: Notificaciones de nuevas licitaciones compatibles
- **Machine Learning**: Modelo personalizado para predicción de éxito

### Consideraciones Éticas
- **Privacidad**: Encriptación de datos sensibles
- **Transparencia**: Explicabilidad de scores generados
- **Auditoría**: Logs detallados para compliance

Este proyecto demuestra la viabilidad de sistemas RAG modernos para automatizar tareas empresariales complejas, combinando lo mejor de la IA generativa con recuperación de información eficiente.