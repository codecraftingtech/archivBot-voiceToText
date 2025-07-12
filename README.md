# archivBot-voiceToText

Pequeña API en Flask que utiliza Whisper para convertir audio a texto.

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

Iniciar el servidor:

```bash
python app.py
```

### Solicitud de transcripción

Enviar un archivo `.mp3` (máximo 1MB):

```bash
curl -X POST -F "file=@audio.mp3" http://localhost:5000/transcribe
```

La respuesta será un JSON con el texto transcrito.
