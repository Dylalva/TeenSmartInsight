# Web Application Documentation

## Application Overview

The TeenSmartInsight web application is a Flask-based application that provides a user-friendly interface for collecting technology usage data from adolescents, analyzing it using the trained machine learning model, and providing personalized recommendations using the Google Gemini API.

## Architecture

The application follows a Model-View-Controller (MVC) architecture:

```
App/
├── app/
│   ├── controllers/     # Request handling and business logic
│   ├── models/          # Data models and prediction logic
│   ├── services/        # External service integrations
│   ├── static/          # CSS, JavaScript, and other static files
│   ├── templates/       # HTML templates
│   ├── utils/           # Helper functions and form definitions
│   └── __init__.py      # Application factory
├── data/                # Data storage
├── model/               # Trained model files
├── .env                 # Environment variables
├── docker-compose.yml   # Docker configuration
├── Dockerfile           # Docker build instructions
└── run.py               # Application entry point
```

## Key Components

### Controllers

The main controller (`main_controller.py`) handles HTTP requests and responses:

- `index()`: Handles the main page, form submission, and prediction display
- `about()`: Renders the about page
- Error handlers for 404 and 500 errors

### Models

The prediction model (`prediction_model.py`) handles the machine learning model integration:

- Loads the trained Random Forest model from the pickle file
- Processes user input data
- Makes predictions about addiction levels
- Stores prediction results in a CSV file for future analysis

### Services

The application integrates with external services:

- `gemini_service.py`: Integrates with Google Gemini API for AI-powered analysis
- `mock_analysis_service.py`: Provides fallback analysis when Gemini API is unavailable

### Forms

The application uses Flask-WTF for form handling (`forms.py`):

- Collects user data on technology usage habits
- Validates input data (e.g., range constraints)
- Provides user-friendly input fields with placeholders

## User Flow

1. **Data Collection**: Users fill out a form with information about their technology usage habits
2. **Prediction**: The application processes the data using the trained machine learning model
3. **AI Analysis**: The application sends the data and prediction to the Google Gemini API
4. **Results Display**: The application displays the prediction and personalized recommendations
5. **Data Storage**: The prediction is stored for future analysis and model improvement

## Environment Variables

The application requires the following environment variables:

- `GEMINI_API_KEY`: API key for Google Gemini
- `DATABASE_PATH`: Path to the CSV file for storing predictions
- `SECRET_KEY`: Secret key for Flask session security

## Docker Deployment

The application can be deployed using Docker:

```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build and run manually
docker build -t teensmart-app .
docker run -p 5000:5000 -v ./data:/app/data --env-file .env teensmart-app
```

The Docker configuration includes:

- Python 3.10 base image
- Installation of dependencies from requirements.txt
- Volume mounting for persistent data storage
- Port mapping for the web interface

## References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/)
- [Google Gemini API Documentation](https://ai.google.dev/docs/gemini_api)
- [Docker Documentation](https://docs.docker.com/)