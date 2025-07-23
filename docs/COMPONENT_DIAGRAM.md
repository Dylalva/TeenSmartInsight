# TeenSmartInsight Component Diagrams

## System Component Diagram

This diagram shows the main components of the TeenSmartInsight system and how they relate to each other.

```mermaid
classDiagram
    WebApplication --> Controllers : uses
    Controllers --> Forms : validates
    Controllers --> PredictionModel : gets prediction
    Controllers --> GeminiService : gets analysis
    Controllers --> MockAnalysisService : fallback
    PredictionModel --> RandomForestModel : uses
    PredictionModel --> DataStorage : stores results
    GeminiService --> GeminiAPI : calls
    
    class WebApplication {
        +Flask app
        +Templates
        +Static files
        +create_app()
    }
    
    class Controllers {
        +main_bp: Blueprint
        +index()
        +about()
        +handle_errors()
    }
    
    class Forms {
        +PredictionForm
        +validate_input()
    }
    
    class PredictionModel {
        -pipeline
        -features
        -database_path
        +predict()
        -_save_prediction()
        -_load_pipeline()
    }
    
    class GeminiService {
        -api_key
        +analyze_prediction()
        -_configure_gemini()
    }
    
    class MockAnalysisService {
        +analyze_prediction()
        -_high_risk_template()
        -_moderate_risk_template()
        -_low_risk_template()
    }
    
    class RandomForestModel {
        +fit()
        +predict()
        +feature_importances_
    }
    
    class DataStorage {
        +CSV file
        +read_data()
        +write_data()
    }
    
    class GeminiAPI {
        +Google Gemini API
    }
```
```

## Layered Architecture Diagram

This diagram shows the layered architecture of the TeenSmartInsight system.

```mermaid
graph TD
    A[Presentation Layer] --> B[Controller Layer]
    B --> C[Service Layer]
    B --> D[Model Layer]
    C --> E[External APIs]
    D --> F[Data Layer]
    
    subgraph PresentationLayer["Presentation Layer"]
        A1[HTML Templates]
        A2[CSS/JavaScript]
    end
    
    subgraph ControllerLayer["Controller Layer"]
        B1[main_controller.py]
    end
    
    subgraph ServiceLayer["Service Layer"]
        C1[gemini_service.py]
        C2[mock_analysis_service.py]
    end
    
    subgraph ModelLayer["Model Layer"]
        D1[prediction_model.py]
    end
    
    subgraph ExternalAPIs["External APIs"]
        E1[Google Gemini API]
    end
    
    subgraph DataLayer["Data Layer"]
        F1[CSV Storage]
        F2[Machine Learning Model]
    end
    
    A --> A1
    A --> A2
    B --> B1
    C --> C1
    C --> C2
    D --> D1
    E --> E1
    F --> F1
    F --> F2
```
```

## Prediction Sequence Diagram

This diagram shows the sequence of operations that occur when a user requests a prediction.

```mermaid
sequenceDiagram
    actor User
    participant WebUI as Web Interface
    participant Controller as MainController
    participant Form as PredictionForm
    participant Model as PredictionModel
    participant ML as ML Pipeline
    participant AI as GeminiService
    participant DB as Data Storage
    
    User->>WebUI: Enters usage data
    WebUI->>Controller: Submits form
    Controller->>Form: Validates data
    Form-->>Controller: Validated data
    Controller->>Model: Requests prediction
    Model->>ML: Processes data
    ML-->>Model: Returns prediction
    Model->>DB: Saves prediction
    Controller->>AI: Requests analysis
    AI-->>Controller: Returns recommendations
    Controller->>WebUI: Displays results
    WebUI-->>User: Views prediction and recommendations
```