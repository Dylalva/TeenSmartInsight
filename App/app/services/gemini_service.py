import os
import google.generativeai as genai
from dotenv import load_dotenv
import markdown2

class GeminiService:
    """Servicio para interactuar con la API de Gemini"""
    
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('GEMINI_API_KEY')
        self._configure_gemini()
    
    def _configure_gemini(self):
        """Configura la API de Gemini"""
        if self.api_key:
            genai.configure(api_key=self.api_key)
        else:
            print("Advertencia: No se ha configurado la API key de Gemini")
    
    def analyze_prediction(self, user_data, prediction):
        """
        Analiza los datos del usuario y la predicción usando Gemini
        
        Args:
            user_data (dict): Datos ingresados por el usuario
            prediction: Resultado de la predicción del modelo
            
        Returns:
            str: Análisis generado por Gemini
        """
        if not self.api_key:
            return "No se pudo conectar con Gemini. Verifique la API key."
        
        try:
            # Crear el modelo (usando el nombre correcto del modelo)
            model = genai.GenerativeModel('gemini-1.5-pro')
            
            # Preparar el prompt para Gemini
            prompt = f"""
            Analiza los siguientes datos de uso de tecnología de un adolescente y proporciona recomendaciones:
            
            - Horas de uso diario: {user_data['Daily_Usage_Hours']}
            - Aplicaciones usadas diariamente: {user_data['Apps_Used_Daily']}
            - Tiempo en redes sociales (horas): {user_data['Time_on_Social_Media']}
            - Tiempo en juegos (horas): {user_data['Time_on_Gaming']}
            - Veces que revisa el teléfono al día: {user_data['Phone_Checks_Per_Day']}
            - Horas de sueño: {user_data['Sleep_Hours']}
            - Horas de uso en fin de semana: {user_data['Weekend_Usage_Hours']}
            - Rendimiento académico (escala 1-10): {user_data['Academic_Performance']}
            
            El modelo de predicción indica que el nivel de adicción tecnológica es: {prediction}
            
            Por favor proporciona:
            1. Un análisis breve del patrón de uso tecnológico
            2. Recomendaciones específicas para mejorar hábitos digitales
            3. Posibles señales de alerta que deberían atenderse
            """
            
            # Generar la respuesta
            response = model.generate_content(prompt)
            
            # Convertir Markdown a HTML
            html_content = markdown2.markdown(response.text, extras=["tables", "fenced-code-blocks"])
            return html_content
            
        except Exception as e:
            return f"Error al conectar con Gemini: {str(e)}"