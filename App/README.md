<details>
<summary><h2>English</h2></summary>

# TeenSmartInsight

Web application for analyzing adolescents’ technology usage habits and assessing potential levels of technology addiction.

## Features

* Form to collect data on technology usage habits
* Machine learning model to predict technology addiction levels
* Integration with Gemini for detailed analysis and personalized recommendations
* Storage of predictions in CSV format for further analysis

## Requirements

* Python 3.8 or higher
* Pip (Python package manager)
* Google Gemini API Key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Dylalva/TeenSmartInsight.git
   cd TeenSmartInsight/App
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   * On Windows:

     ```bash
     venv\Scripts\activate
     ```
   * On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure environment variables:

   * Copy `.env.example` to `.env`
   * Edit `.env` and add your Google Gemini API Key

## Usage

### Running Locally

1. Start the application:

   ```bash
   python run.py
   ```
2. Open your web browser and go to:

   ```
   http://localhost:5000
   ```

### Running with Docker

1. Build and run with Docker Compose:

   ```bash
   docker-compose up -d
   ```

   Or use this command to build and run the container directly:

   ```bash
   docker run -d --name teensmart -p 5000:5000 dylalva/app-teensmart
   ```

2. Open your web browser and go to:

   ```
   http://localhost:5000
   ```

3. To stop the application:

   ```bash
   docker-compose down
   ```

### Using the Application

Fill out the form with the requested data and click **Analyze** to get your results.

## Project Structure

```
TeenSmartInsight/App/
├── app/                    # Main application directory
│   ├── controllers/        # Route handlers
│   ├── models/             # Business logic models
│   ├── services/           # External integration services
│   ├── static/             # Static files (CSS, JS, images)
│   ├── templates/          # HTML templates
│   └── utils/              # Utilities and helper modules
├── data/                   # Directory for storing data
├── model/                  # Directory containing the trained model
├── .dockerignore           # Files to ignore in Docker context
├── .env                    # Environment variables
├── .env.example            # Example environment variables
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Docker image build instructions
├── requirements.txt        # Project dependencies
└── run.py                  # Application entry point
```

## License

This project is licensed under the [MIT License](../LICENSE).

</details>


<details>
<summary><h2>Español</h2></summary>

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
git clone https://github.com/Dylalva/TeenSmartInsight.git
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
O bien puedes utilizar el siguiente comando que construye la aplicación:

```Bash
docker run -d --name teensmart -p 5000:5000 dylalva/app-teensmart
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

Este proyecto está licenciado bajo la [Licencia MIT](../LICENSE)

</details>