# -*- coding: utf-8 -*-
"""Aplicación de reconocimiento de entidades nombradas (NER) en español.

Esta API utiliza FastAPI y la librería de procesamiento de lenguaje natural
spaCy con el modelo ``es_core_news_sm`` para identificar entidades en un texto.
Funciona en macOS, Windows y Linux.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import spacy

# Cargamos el modelo de spaCy para español una única vez al iniciar la app.
# Esto evita recargarlo en cada petición y mejora el rendimiento.
nlp = spacy.load("es_core_news_sm")

# Creamos la instancia de la aplicación FastAPI.
app = FastAPI(title="API NER en español")


class Texto(BaseModel):
    """Estructura de los datos de entrada.

    Espera un JSON con una clave ``text`` que contenga el texto a analizar.
    """

    text: str


@app.post("/ner")
def obtener_entidades(data: Texto):
    """Extrae las entidades nombradas del texto recibido.

    Args:
        data (Texto): Objeto con el texto a analizar.

    Returns:
        dict: Diccionario con una lista de entidades encontradas.
    """

    # Procesamos el texto con el modelo de spaCy para obtener las entidades.
    documento = nlp(data.text)

    # Construimos una lista con la información relevante de cada entidad.
    entidades = [
        {
            "text": entidad.text,       # Texto exacto de la entidad
            "label": entidad.label_,    # Tipo de entidad (persona, lugar, etc.)
            "start": entidad.start_char, # Posición inicial en el texto
            "end": entidad.end_char      # Posición final en el texto
        }
        for entidad in documento.ents
    ]

    # Devolvemos las entidades en formato JSON.
    return {"entities": entidades}
