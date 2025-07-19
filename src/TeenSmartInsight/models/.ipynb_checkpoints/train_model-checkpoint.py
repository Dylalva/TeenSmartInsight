import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer

def train_and_save_model(input_path: str, model_path: str):
    df = pd.read_csv(input_path)
    
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
    X = df[features]
    y = df['Addiction_Level']


    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), features),
    ])

    pipeline = Pipeline([
        ('preproc', preprocessor),
        ('model', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    pipeline.fit(X, y)



    joblib.dump(pipeline, model_path)

if __name__ == '__main__':
    input_path = os.getenv(
        'PROCESSED_DATA_PATH',
        './data/raw/teen_phone_addiction_dataset.csv'
    )
    model_path = os.getenv(
        'MODEL_OUTPUT_PATH',
        './models/rf_pipeline.pkl'
    )
    train_and_save_model(input_path, model_path)