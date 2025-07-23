# TeenSmartInsight Project Structure

This document provides a visual representation of the TeenSmartInsight project structure using multiple diagrams for better readability.

## Main Project Structure

The following diagram shows the top-level directories of the TeenSmartInsight project:

```mermaid
graph TD
    A[TeenSmartInsight] --> B[App]
    A --> C[data]
    A --> D[figures]
    A --> E[infrastructure]
    A --> F[models]
    A --> G[notebooks]
    A --> H[scripts]
    A --> I[src]
    A --> J[docs]
```

## Web Application Structure

The following diagram shows the structure of the Flask web application:

```mermaid
graph TD
    B[App] --> B1[app]
    B --> B2[data]
    B --> B3[model]
    B --> B4[Dockerfile]
    B --> B5[docker-compose.yml]
    B --> B6[run.py]
    B --> B7[requirements.txt]
```

## Application Core Structure

The following diagram shows the internal structure of the Flask application:

```mermaid
graph TD
    B1[app] --> B1A[controllers]
    B1 --> B1B[models]
    B1 --> B1C[services]
    B1 --> B1D[static]
    B1 --> B1E[templates]
    B1 --> B1F[utils]
    
    B1A --> B1A1[main_controller.py]
    B1B --> B1B1[prediction_model.py]
    B1C --> B1C1[gemini_service.py]
    B1C --> B1C2[mock_analysis_service.py]
```

## Templates and Static Files

The following diagram shows the structure of templates and static files:

```mermaid
graph TD
    B1D[static] --> B1D1[css]
    B1D --> B1D2[js]
    B1D1 --> B1D1A[style.css]
    B1D2 --> B1D2A[main.js]
    
    B1E[templates] --> B1E1[base.html]
    B1E --> B1E2[index.html]
    B1E --> B1E3[about.html]
    B1E --> B1E4[404.html]
    B1E --> B1E5[500.html]
    
    B1F[utils] --> B1F1[forms.py]
    B1F --> B1F2[filters.py]
```

## Data and Model Structure

The following diagram shows the structure of data and model directories:

```mermaid
graph TD
    C[data] --> C1[raw]
    C1 --> C1A[teen_phone_addiction_dataset.csv]
    
    F[models] --> F1[rf_pipeline.pkl]
```

## Source Code Structure

The following diagram shows the structure of the source code directory:

```mermaid
graph TD
    I[src] --> I1[TeenSmartInsight]
    I1 --> I1A[models]
    I1A --> I1A1[train_model.py]
    I1A --> I1A2[evaluate_model.py]
```

## Infrastructure and Documentation

The following diagram shows the structure of infrastructure and documentation directories:

```mermaid
graph TD
    E[infrastructure] --> E1[main.tf]
    E --> E2[deploy-with-docker.yml]
    E --> E3[hosts.ini]
    
    J[docs] --> J1[index.md]
    J --> J2[MODEL.md]
    J --> J3[APP.md]
    J --> J4[INFRASTRUCTURE.md]
    J --> J5[API.md]
    J --> J6[PROJECT_STRUCTURE.md]
    J --> J7[WORKFLOW_DIAGRAM.md]
    J --> J8[COMPONENT_DIAGRAM.md]
```

## Key Components Description

1. **App**: Contains the Flask web application
   - **app**: Core application code (MVC structure)
   - **data**: Stores prediction results
   - **model**: Contains the trained machine learning model

2. **data**: Contains the raw dataset used for model training

3. **figures**: Contains visualizations and demo materials

4. **infrastructure**: Contains AWS deployment configuration
   - **main.tf**: Terraform configuration
   - **deploy-with-docker.yml**: Ansible deployment playbook

5. **models**: Contains the trained machine learning model

6. **notebooks**: Contains Jupyter notebooks for data analysis

7. **scripts**: Contains utility scripts for running tests and training

8. **src**: Contains the source code for model training and evaluation

9. **docs**: Contains project documentation