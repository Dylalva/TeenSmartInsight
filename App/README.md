# TeenSmartInsight

Aplicación web para analizar hábitos de uso de tecnología en adolescentes y evaluar posibles niveles de adicción tecnológica.

## Características

- Formulario para recopilar datos sobre hábitos de uso de tecnología
- Modelo de machine learning para predecir niveles de adicción tecnológica
- Integración con Gemini para análisis detallado y recomendaciones personalizadas
- Almacenamiento de predicciones en formato CSV para análisis posterior

## Requisitos

- Python 3.8 o superior
- Pip (gestor de paquetes de Python)
- API Key de Google Gemini

## Instalación

1. Clonar el repositorio:
```
git clone <url-del-repositorio>
cd TeenSmartInsight/App
```

2. Crear un entorno virtual:
```
python -m venv venv
```

3. Activar el entorno virtual:
   - En Windows:
   ```
   venv\Scripts\activate
   ```
   - En macOS/Linux:
   ```
   source venv/bin/activate
   ```

4. Instalar las dependencias:
```
pip install -r requirements.txt
```

5. Configurar las variables de entorno:
   - Copiar el archivo `.env.example` a `.env`
   - Editar el archivo `.env` y añadir la API Key de Gemini

## Uso

### Ejecución local

1. Iniciar la aplicación:
```
python run.py
```

2. Abrir un navegador web y acceder a:
```
http://localhost:5000
```

### Ejecución con Docker

1. Construir y ejecutar con Docker Compose:
```
docker-compose up -d
```

2. Abrir un navegador web y acceder a:
```
http://localhost:5000
```

3. Para detener la aplicación:
```
docker-compose down
```

### Uso de la aplicación

Completar el formulario con los datos solicitados y hacer clic en "Analizar" para obtener resultados.

## Estructura del Proyecto

```
TeenSmartInsight/App/
├── app/                    # Directorio principal de la aplicación
│   ├── controllers/        # Controladores para manejar las rutas
│   ├── models/             # Modelos para la lógica de negocio
│   ├── services/           # Servicios para integraciones externas
│   ├── static/             # Archivos estáticos (CSS, JS, imágenes)
│   ├── templates/          # Plantillas HTML
│   └── utils/              # Utilidades y herramientas
├── data/                   # Directorio para almacenar datos
├── model/                  # Directorio con el modelo entrenado
├── .dockerignore           # Archivos a ignorar en el contexto de Docker
├── .env                    # Variables de entorno
├── .env.example            # Ejemplo de variables de entorno
├── docker-compose.yml      # Configuración para Docker Compose
├── Dockerfile              # Instrucciones para construir la imagen Docker
├── requirements.txt        # Dependencias del proyecto
└── run.py                  # Punto de entrada de la aplicación
```

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.