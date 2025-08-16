# archivBot-voiceToText

Voice to text

## API de Reconocimiento de Entidades (NER)

Esta API en Python utiliza FastAPI y spaCy con el modelo `es_core_news_sm`
para extraer entidades nombradas de un texto en español.

### Requisitos

1. Python 3.9 o superior (macOS, Windows o Linux).
2. Instalar las dependencias:

```bash
pip install -r requerimiento.txt
```

### Ejecutar la API

Iniciar el servidor con:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Probar con cURL

```bash
curl -X POST "http://localhost:8000/ner" \
     -H "Content-Type: application/json" \
     -d '{"text": "Barack Obama nació en Estados Unidos"}'
```

El comando devolverá un JSON con las entidades reconocidas.
