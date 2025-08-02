# archivBot-voiceToText
Voice to text

# comando ejecutar instalar las librerías
pip install -r requirements.txt
# comando para ejecutar la aplicación
python archivBot-voiceToText.py
# CURL
curl -X POST -F "file=@audios/saludo_prueba1.m4a" http://localhost:5000/transcribe