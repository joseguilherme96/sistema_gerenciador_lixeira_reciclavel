# Configurando o SocketIO
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os

load_dotenv()

socketio = SocketIO(cors_allowed_origins= os.getenv('ORIGENS_PERMITIDAS').split(','))



