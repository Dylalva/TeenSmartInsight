# Data Analysis and Model Documentation

## Dataset Overview

The TeenSmartInsight project uses a dataset that captures various aspects of adolescent technology usage and its potential impact on their well-being. The dataset includes the following key features:

- **Demographics**: Age, gender, location, school grade
- **Technology Usage**: Daily usage hours, apps used daily, time on social media, time on gaming
- **Behavioral Indicators**: Sleep hours, phone checks per day, weekend usage hours
- **Well-being Metrics**: Academic performance, anxiety level, depression level, self-esteem
- **Target Variable**: Addiction level (scale of 1-10)

## Exploratory Data Analysis

The exploratory data analysis (EDA) is performed in the Jupyter notebook `001_TeenAddiction.ipynb`. The analysis includes:

1. **Data Cleaning and Preprocessing**:
   - Handling missing values
   - Encoding categorical variables
   - Feature scaling

2. **Statistical Analysis**:
   - Descriptive statistics of key variables
   - Correlation analysis between technology usage and addiction levels
   - Distribution analysis of addiction levels across different demographics

3. **Visualization**:
   - Heatmaps showing correlation between variables
   - Scatter plots showing relationships between usage patterns and addiction levels
   - Bar charts comparing addiction levels across different demographics

Key visualizations from the analysis can be found in the `figures/` directory, including:
- `mapaCalorCorrelacion.png`: Correlation heatmap between variables
- `catNumRespecto_AddLvl.png`: Categorical and numerical variables with respect to addiction level

## Machine Learning Model

### Model Selection

After evaluating several machine learning algorithms, a **Random Forest Regressor** was selected for the following reasons:

- Ability to handle non-linear relationships
- Robustness to outliers
- Feature importance capabilities
- Good performance with moderate-sized datasets

### Feature Engineering

The following features were selected for the model based on their correlation with addiction levels and domain knowledge:

```python
features = [
    'Daily_Usage_Hours',
    'Apps_Used_Daily',
    'Time_on_Social_Media',
    'Time_on_Gaming',
    'Phone_Checks_Per_Day',
    'Sleep_Hours',
    'Weekend_Usage_Hours',
    'Academic_Performance'
]
```

### Model Pipeline

The model uses a scikit-learn pipeline that includes:

1. **Preprocessing**: StandardScaler for numerical features
2. **Model**: RandomForestRegressor with 100 estimators

```python
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), features),
])

pipeline = Pipeline([
    ('preproc', preprocessor),
    ('model', RandomForestRegressor(n_estimators=100, random_state=42))
])
```

### Model Evaluation

The model is evaluated using the following metrics:

- **Mean Squared Error (MSE)**: Measures the average squared difference between predicted and actual addiction levels
- **Mean Absolute Error (MAE)**: Measures the average absolute difference between predicted and actual addiction levels
- **R-squared (R²)**: Measures the proportion of variance in addiction levels explained by the model

The evaluation script (`evaluate_model.py`) also generates a scatter plot comparing predicted vs. actual addiction levels.

### Model Deployment

The trained model is serialized using joblib and saved as `rf_pipeline.pkl`. This file is then used by the web application to make predictions based on user input.

## References

- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Random Forest Algorithm](https://scikit-learn.org/stable/modules/ensemble.html#forest)
- [Feature Scaling](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Pipeline API](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)