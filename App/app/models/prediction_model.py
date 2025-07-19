import os
import pandas as pd
import pickle
from datetime import datetime

class PredictionModel:
    """Modelo para manejar las predicciones y almacenar los resultados"""
    
    def __init__(self, app=None):
        self.pipeline = None
        self.features = [
            'Daily_Usage_Hours',
            'Apps_Used_Daily',
            'Time_on_Social_Media',
            'Time_on_Gaming',
            'Phone_Checks_Per_Day',
            'Sleep_Hours',
            'Weekend_Usage_Hours',
            'Academic_Performance'
        ]
        self.database_path = os.getenv('DATABASE_PATH', 'data/predictions.csv')
        self._load_pipeline()
        self._initialize_database()
    
    def _load_pipeline(self):
        """Carga el pipeline con el modelo entrenado"""
        try:
            model_path = os.path.join('model', 'rf_pipeline.pkl')
            with open(model_path, 'rb') as f:
                self.pipeline = pickle.load(f)
        except Exception as e:
            print(f"Error al cargar el modelo: {e}")
            self.pipeline = None
    
    def _initialize_database(self):
        """Inicializa la base de datos CSV si no existe"""
        if not os.path.exists(self.database_path):
            columns = self.features + ['prediction', 'timestamp']
            df = pd.DataFrame(columns=columns)
            os.makedirs(os.path.dirname(self.database_path), exist_ok=True)
            df.to_csv(self.database_path, index=False)
    
    def predict(self, data):
        """Realiza una predicción basada en los datos de entrada"""
        if self.pipeline is None:
            return "No se pudo cargar el modelo"
        
        try:
            # Convertir los datos a un DataFrame
            input_data = pd.DataFrame([data])
            
            # Calcular un puntaje de adicción basado en los datos
            daily_usage = float(data['Daily_Usage_Hours'])
            social_media = float(data['Time_on_Social_Media'])
            gaming = float(data['Time_on_Gaming'])
            phone_checks = int(data['Phone_Checks_Per_Day'])
            sleep = float(data['Sleep_Hours'])
            weekend = float(data['Weekend_Usage_Hours'])
            academic = float(data['Academic_Performance'])
            
            # Fórmula simple para calcular el nivel de adicción
            score = daily_usage + social_media + gaming + (weekend/7) + (phone_checks/50) - sleep - (academic/2)
            
            # Determinar el nivel de adicción basado en el puntaje
            if score > 10:
                prediction = "Alto riesgo de adicción tecnológica (Puntaje: {:.1f})".format(score)
            elif score > 5:
                prediction = "Riesgo moderado de adicción tecnológica (Puntaje: {:.1f})".format(score)
            else:
                prediction = "Bajo riesgo de adicción tecnológica (Puntaje: {:.1f})".format(score)
            
            # Guardar la predicción en la base de datos
            self._save_prediction(data, prediction)
            
            return prediction
            
        except Exception as e:
            print(f"Error al realizar la predicción: {e}")
            return "Error al procesar los datos"
    
    def _save_prediction(self, data, prediction):
        """Guarda la predicción en el archivo CSV"""
        try:
            # Añadir la predicción y timestamp a los datos
            data['prediction'] = prediction
            data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Cargar el CSV existente y añadir la nueva fila
            df = pd.read_csv(self.database_path)
            df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
            
            # Guardar el DataFrame actualizado
            df.to_csv(self.database_path, index=False)
            
            return True
        except Exception as e:
            print(f"Error al guardar la predicción: {e}")
            return False