from flask import Flask, request, jsonify
import whisper
import os
import tempfile

app = Flask(__name__)

# Cargamos el modelo 'base' de Whisper al iniciar la aplicación
# Esto evita recargarlo en cada solicitud
model = whisper.load_model("base")

# Tamaño máximo permitido para el archivo mp3 (1MB)
MAX_FILE_SIZE = 1 * 1024 * 1024

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    """Recibe un archivo mp3 y devuelve su transcripción en texto."""
    if 'file' not in request.files:
        return jsonify({'error': 'Archivo no proporcionado'}), 400

    file = request.files['file']

    # Verificamos el tamaño del archivo
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)
    if size > MAX_FILE_SIZE:
        return jsonify({'error': 'El archivo supera el límite de 1MB'}), 400

    # Guardamos temporalmente el archivo para procesarlo con Whisper
    with tempfile.NamedTemporaryFile(suffix='.mp3') as tmp:
        file.save(tmp.name)
        result = model.transcribe(tmp.name)

    return jsonify({'text': result['text']})

if __name__ == '__main__':
    # Ejecutamos la aplicación de desarrollo
    app.run(host='0.0.0.0', port=5000, debug=True)
