import os
import joblib
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def evaluate_model(model_path: str, processed_data: str):
    # 1. Carga del pipeline y del LabelEncoder
    pipeline = joblib.load(model_path)

    # 2. Carga de datos
    df = pd.read_csv(processed_data)
    
    # 3. Solo las 8 features con las que entrenamos
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

    y_pred = pipeline.predict(X)
    mse = mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    r2  = r2_score(y, y_pred)

    print(f"MSE:  {mse:.3f}")
    print(f"MAE:  {mae:.3f}")
    print(f"R2:   {r2:.3f}")
    plt.figure(figsize=(6,6))
    plt.scatter(y, y_pred, alpha=0.6)
    plt.plot([0,10], [0,10], 'r--')
    plt.xlim(0,10); plt.ylim(0,10)
    plt.xlabel('Valor real')
    plt.ylabel('Predicción')
    plt.title('Real vs Predicho')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    evaluate_model(
        os.getenv('MODEL_PATH', './models/rf_pipeline.pkl'),
        os.getenv('PROCESSED_DATA_PATH', './data/raw/teen_phone_addiction_dataset.csv')
    )
