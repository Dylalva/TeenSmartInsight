# TeenSmartInsight

<details>
<summary><h2>English</h2></summary>

# TeenSmartInsight

A comprehensive project for analyzing adolescents' technology usage habits and assessing potential levels of technology addiction using machine learning and AI.

## Project Overview

TeenSmartInsight is a data science and web application project that combines exploratory data analysis, machine learning modeling, and a user-friendly web interface to help identify and address technology addiction in adolescents.

## Project Structure

The project is organized into several key components:

```
TeenSmartInsight/
├── App/                    # Web application
├── data/                   # Data directory
│   └── raw/                # Raw dataset files
├── figures/                # Visualization outputs
├── models/                 # Trained models
├── notebooks/              # Jupyter notebooks for analysis
├── scripts/                # Utility scripts
└── src/                    # Source code for model training
    └── TeenSmartInsight/   # Core package
        └── models/         # Model training and evaluation
```

### Key Components

#### 1. Data Analysis and Model Development

- **Notebooks**: Contains Jupyter notebooks for exploratory data analysis, feature engineering, and model development
  - `001_TeenAddiction.ipynb`: Main analysis notebook that explores the dataset, visualizes relationships, and develops the prediction model

- **Source Code**: Modular Python code for model training and evaluation
  - `train_model.py`: Script for training the Random Forest regression model
  - `evaluate_model.py`: Script for evaluating model performance

#### 2. Web Application (App/)

- **Flask Application**: Web interface for users to input their technology usage data
  - Collects data through a user-friendly form
  - Processes data using the trained machine learning model
  - Integrates with Google Gemini API for detailed analysis and personalized recommendations
  - Stores predictions for further analysis

- **Docker Support**: Containerization for easy deployment
  - `Dockerfile` and `docker-compose.yml` for containerized deployment

## Functionality

### 1. Data Analysis

The project begins with exploratory data analysis of adolescent technology usage patterns, examining:
- Daily usage hours
- Social media and gaming time
- Sleep patterns
- Academic performance
- Phone checking frequency
- Weekend usage patterns

### 2. Machine Learning Model

- Uses a **Random Forest Regressor** to predict technology addiction levels
- Features engineered from usage patterns and behavioral indicators
- Model evaluation using MSE, MAE, and R² metrics

### 3. Web Application

- **Input Form**: Collects user data on technology usage habits
- **Prediction Engine**: Processes data through the trained model
- **AI Analysis**: Integrates with Google Gemini for personalized recommendations
- **Data Storage**: Saves predictions for future analysis and model improvement

## Technologies Used

- **Data Analysis**: Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning**: Scikit-learn, Joblib
- **Web Development**: Flask, Bootstrap
- **AI Integration**: Google Gemini API
- **Deployment**: Docker, Docker Compose

## License

This project is licensed under the [MIT License](LICENSE).

</details>


<details>
<summary><h2>Español</h2></summary>

# TeenSmartInsight

Un proyecto integral para analizar los hábitos de uso de tecnología en adolescentes y evaluar posibles niveles de adicción tecnológica utilizando machine learning e IA.

## Visión General del Proyecto

TeenSmartInsight es un proyecto de ciencia de datos y aplicación web que combina análisis exploratorio de datos, modelado de machine learning y una interfaz web fácil de usar para ayudar a identificar y abordar la adicción tecnológica en adolescentes.

## Estructura del Proyecto

El proyecto está organizado en varios componentes clave:

```
TeenSmartInsight/
├── App/                    # Aplicación web
├── data/                   # Directorio de datos
│   └── raw/                # Archivos de datos sin procesar
├── figures/                # Salidas de visualización
├── models/                 # Modelos entrenados
├── notebooks/              # Notebooks Jupyter para análisis
├── scripts/                # Scripts de utilidad
└── src/                    # Código fuente para entrenamiento de modelos
    └── TeenSmartInsight/   # Paquete principal
        └── models/         # Entrenamiento y evaluación de modelos
```

### Componentes Principales

#### 1. Análisis de Datos y Desarrollo del Modelo

- **Notebooks**: Contiene notebooks Jupyter para análisis exploratorio de datos, ingeniería de características y desarrollo del modelo
  - `001_TeenAddiction.ipynb`: Notebook principal de análisis que explora el conjunto de datos, visualiza relaciones y desarrolla el modelo de predicción

- **Código Fuente**: Código Python modular para entrenamiento y evaluación de modelos
  - `train_model.py`: Script para entrenar el modelo de regresión Random Forest
  - `evaluate_model.py`: Script para evaluar el rendimiento del modelo

#### 2. Aplicación Web (App/)

- **Aplicación Flask**: Interfaz web para que los usuarios ingresen sus datos de uso de tecnología
  - Recopila datos a través de un formulario fácil de usar
  - Procesa datos utilizando el modelo de machine learning entrenado
  - Se integra con la API de Google Gemini para análisis detallados y recomendaciones personalizadas
  - Almacena predicciones para análisis posterior

- **Soporte Docker**: Containerización para facilitar el despliegue
  - `Dockerfile` y `docker-compose.yml` para despliegue containerizado

## Funcionalidad

### 1. Análisis de Datos

El proyecto comienza con un análisis exploratorio de datos de patrones de uso de tecnología en adolescentes, examinando:
- Horas de uso diario
- Tiempo en redes sociales y juegos
- Patrones de sueño
- Rendimiento académico
- Frecuencia de revisión del teléfono
- Patrones de uso en fin de semana

### 2. Modelo de Machine Learning

- Utiliza un **Random Forest Regressor** para predecir niveles de adicción tecnológica
- Características diseñadas a partir de patrones de uso e indicadores de comportamiento
- Evaluación del modelo utilizando métricas MSE, MAE y R²

### 3. Aplicación Web

- **Formulario de Entrada**: Recopila datos del usuario sobre hábitos de uso de tecnología
- **Motor de Predicción**: Procesa datos a través del modelo entrenado
- **Análisis de IA**: Se integra con Google Gemini para recomendaciones personalizadas
- **Almacenamiento de Datos**: Guarda predicciones para análisis futuro y mejora del modelo

## Tecnologías Utilizadas

- **Análisis de Datos**: Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning**: Scikit-learn, Joblib
- **Desarrollo Web**: Flask, Bootstrap
- **Integración de IA**: API de Google Gemini
- **Despliegue**: Docker, Docker Compose

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

</details>