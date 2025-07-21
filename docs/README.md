# TeenSmartInsight Documentation

## Project Overview

TeenSmartInsight is a comprehensive data science and web application project designed to analyze adolescents' technology usage habits and assess potential levels of technology addiction using machine learning and AI. The project combines exploratory data analysis, machine learning modeling, and a user-friendly web interface to help identify and address technology addiction in adolescents.

## Documentation Sections

- [Data Analysis and Model Documentation](MODEL.md) - Details about the dataset, exploratory data analysis, and machine learning model
- [Web Application Documentation](APP.md) - Information about the Flask application, its architecture, and features
- [Infrastructure Documentation](INFRASTRUCTURE.md) - Details about AWS deployment, Docker containerization, and CI/CD pipeline
- [API Documentation](API.md) - Information about the Gemini API integration and other services

## Key Features

- **Data-Driven Analysis**: Comprehensive analysis of adolescent technology usage patterns
- **Machine Learning Prediction**: Random Forest model to predict technology addiction levels
- **AI-Powered Recommendations**: Integration with Google Gemini API for personalized insights
- **User-Friendly Interface**: Easy-to-use web application for data collection and analysis
- **Secure Cloud Deployment**: AWS infrastructure with HTTPS support

## Getting Started

To get started with TeenSmartInsight:

1. Clone the repository
2. Set up the environment variables (see `.env.example`)
3. Install dependencies with `pip install -r requirements.txt`
4. Run the application locally with `python App/run.py`

For more detailed instructions, see the [Application Documentation](APP.md).

## Project Structure

```
TeenSmartInsight/
├── App/                    # Web application
├── data/                   # Data directory
│   └── raw/                # Raw dataset files
├── figures/                # Visualization outputs
├── infrastructure/         # Deployment infrastructure in AWS
├── models/                 # Trained models
├── notebooks/              # Jupyter notebooks for analysis
├── scripts/                # Utility scripts
└── src/                    # Source code for model training
    └── TeenSmartInsight/   # Core package
        └── models/         # Model training and evaluation
```

## License

This project is licensed under the [MIT License](../LICENSE).