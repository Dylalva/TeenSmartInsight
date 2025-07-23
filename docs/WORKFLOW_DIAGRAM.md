# TeenSmartInsight Workflow Diagrams

## Application Workflow

The following diagram shows the workflow of the TeenSmartInsight application, from user data input to recommendation generation.

```mermaid
flowchart TD
    A[User enters data] --> B[Flask Form]
    B --> C{Data validation}
    C -->|Invalid data| B
    C -->|Valid data| D[PredictionModel]
    D --> E[Random Forest Model]
    E --> F[Addiction level prediction]
    F --> G{Analysis service}
    G -->|Gemini API available| H[GeminiService]
    G -->|Gemini API unavailable| I[MockAnalysisService]
    H --> J[Analysis and recommendations]
    I --> J
    J --> K[Display results to user]
    K --> L[Save prediction to CSV]
```

## Model Training Workflow

This diagram shows the machine learning model training process.

```mermaid
flowchart TD
    A[Raw data] --> B[Preprocessing]
    B --> C[Train/test split]
    C --> D[Feature scaling]
    D --> E[Random Forest model training]
    E --> F[Model evaluation]
    F --> G{Acceptable performance?}
    G -->|No| H[Hyperparameter tuning]
    H --> E
    G -->|Yes| I[Model serialization]
    I --> J[Model saved as rf_pipeline.pkl]
```

## Deployment Workflow

This diagram shows the process of deploying the application to AWS.

```mermaid
flowchart TD
    A[Code in GitHub] --> B[GitHub Actions CI/CD]
    B --> C[Build Docker image]
    C --> D[Publish image to Docker Hub]
    D --> E[Terraform creates AWS infrastructure]
    E --> F[Ansible configures server]
    F --> G[Install Docker and dependencies]
    G --> H[Deploy Docker container]
    H --> I[Configure Nginx]
    I --> J[Obtain SSL certificates]
    J --> K[Application in production]
```

## System Architecture

This diagram shows the general architecture of the TeenSmartInsight system.

```mermaid
flowchart TD
    A[Client/Browser] -->|HTTPS| B[Nginx]
    B -->|Reverse proxy| C[Docker Container]
    C -->|Flask App| D[Prediction Model]
    C -->|API| E[Google Gemini API]
    D --> F[Data Storage]
    
    subgraph AWSEC2[AWS EC2]
        B
        C
        D
        F
    end
```