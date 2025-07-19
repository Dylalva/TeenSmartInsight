import os
from flask import Flask
from dotenv import load_dotenv

def create_app():
    """Inicializa y configura la aplicación Flask"""
    # Cargar variables de entorno
    load_dotenv()
    
    # Crear y configurar la aplicación
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['DATABASE_PATH'] = os.getenv('DATABASE_PATH')
    
    # Asegurar que el directorio de datos exista
    os.makedirs(os.path.dirname(app.config['DATABASE_PATH']), exist_ok=True)
    
    # Registrar blueprints
    from app.controllers.main_controller import main_bp
    app.register_blueprint(main_bp)
    
    return app