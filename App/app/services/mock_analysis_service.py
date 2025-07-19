import markdown2

class MockAnalysisService:
    """Servicio alternativo para generar análisis sin depender de APIs externas"""
    
    def analyze_prediction(self, user_data, prediction):
        """
        Genera un análisis basado en los datos del usuario sin usar APIs externas
        
        Args:
            user_data (dict): Datos ingresados por el usuario
            prediction: Resultado de la predicción del modelo
            
        Returns:
            str: Análisis generado
        """
        # Extraer datos relevantes
        daily_usage = float(user_data['Daily_Usage_Hours'])
        social_media = float(user_data['Time_on_Social_Media'])
        gaming = float(user_data['Time_on_Gaming'])
        phone_checks = int(user_data['Phone_Checks_Per_Day'])
        sleep = float(user_data['Sleep_Hours'])
        weekend = float(user_data['Weekend_Usage_Hours'])
        academic = float(user_data['Academic_Performance'])
        
        # Generar análisis básico
        analysis = f"""
# Análisis de Uso Tecnológico

## Patrón de Uso Tecnológico
El adolescente utiliza dispositivos tecnológicos aproximadamente {daily_usage} horas al día, 
aumentando a {weekend} horas durante los fines de semana. Dedica {social_media} horas a redes sociales 
y {gaming} horas a videojuegos diariamente. Revisa su teléfono aproximadamente {phone_checks} veces al día.

## Evaluación
"""
        
        # Evaluar nivel de adicción
        if "Alto riesgo" in prediction:
            analysis += """
El patrón de uso muestra signos claros de dependencia tecnológica. El uso excesivo está afectando 
áreas importantes como el sueño y posiblemente el rendimiento académico.
"""
        elif "moderado" in prediction.lower():
            analysis += """
El patrón de uso muestra algunos signos de dependencia tecnológica, pero aún mantiene cierto equilibrio. 
Es importante establecer límites para evitar que la situación empeore.
"""
        else:
            analysis += """
El patrón de uso parece estar dentro de rangos saludables, aunque siempre es recomendable mantener 
hábitos equilibrados con la tecnología.
"""
        
        # Recomendaciones específicas
        analysis += """
## Recomendaciones para Mejorar Hábitos Digitales

1. **Establecer límites de tiempo**: Usar temporizadores o aplicaciones de control parental para limitar el tiempo de pantalla.
2. **Zonas libres de tecnología**: Designar áreas en el hogar donde no se permitan dispositivos electrónicos.
3. **Descansos regulares**: Implementar la regla 20-20-20 (cada 20 minutos, mirar algo a 20 pies de distancia durante 20 segundos).
4. **Actividades alternativas**: Fomentar hobbies y actividades físicas que no involucren pantallas.
5. **Rutina de sueño**: Evitar el uso de dispositivos al menos una hora antes de dormir.
"""
        
        # Señales de alerta
        analysis += """
## Señales de Alerta

- Irritabilidad o ansiedad cuando no puede acceder a dispositivos
- Pérdida de interés en actividades que antes disfrutaba
- Disminución en el rendimiento académico
- Aislamiento social en la vida real
- Problemas para conciliar el sueño
- Dolor de cabeza, cuello o muñecas frecuentes
"""
        
        # Convertir Markdown a HTML
        html_content = markdown2.markdown(analysis, extras=["tables", "fenced-code-blocks"])
        return html_content