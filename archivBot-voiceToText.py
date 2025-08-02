from flask import Flask, request, jsonify, Response
import whisper
import os
import tempfile
import json

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
    temp_path = save_temp_file(file)
    try:
        result = model.transcribe(temp_path)
        response_json = json.dumps({'text': result['text']}, ensure_ascii=False) + "\n"
    finally:
        try:
            os.remove(temp_path)
        except OSError as e:
            print(f"Error al eliminar archivo temporal: {e}")

    return Response(response_json, content_type="application/json; charset=utf-8")


def save_temp_file(file, suffix=".mp3"):
    tmp = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
    temp_path = tmp.name
    tmp.close()  # Cierra el archivo para evitar bloqueo en Windows
    file.save(temp_path)
    return temp_path

if __name__ == '__main__':
    # Ejecutamos la aplicación de desarrollo
    app.run(host='0.0.0.0', port=5000, debug=True)