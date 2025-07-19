from flask import Blueprint, render_template, request, flash, current_app
from app.utils.forms import PredictionForm
from app.models.prediction_model import PredictionModel
from app.services.gemini_service import GeminiService
from app.services.mock_analysis_service import MockAnalysisService

# Crear el blueprint
main_bp = Blueprint('main', __name__)

# Instanciar el modelo y los servicios
prediction_model = PredictionModel()
gemini_service = GeminiService()
mock_service = MockAnalysisService()

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    """Ruta principal para la página de inicio"""
    form = PredictionForm()
    prediction = None
    analysis = None
    
    if form.validate_on_submit():
        # Recopilar datos del formulario
        user_data = {
            'Daily_Usage_Hours': form.Daily_Usage_Hours.data,
            'Apps_Used_Daily': form.Apps_Used_Daily.data,
            'Time_on_Social_Media': form.Time_on_Social_Media.data,
            'Time_on_Gaming': form.Time_on_Gaming.data,
            'Phone_Checks_Per_Day': form.Phone_Checks_Per_Day.data,
            'Sleep_Hours': form.Sleep_Hours.data,
            'Weekend_Usage_Hours': form.Weekend_Usage_Hours.data,
            'Academic_Performance': form.Academic_Performance.data
        }
        
        # Realizar la predicción
        prediction = prediction_model.predict(user_data)
        
        if prediction is not None:
            # Intentar obtener análisis de Gemini
            analysis = gemini_service.analyze_prediction(user_data, prediction)
            
            # Si hay un error con Gemini, usar el servicio alternativo
            if analysis and analysis.startswith("Error al conectar con Gemini"):
                analysis = mock_service.analyze_prediction(user_data, prediction)
            
            flash('Análisis completado con éxito', 'success')
        else:
            flash('Error al realizar la predicción', 'danger')
    
    return render_template('index.html', form=form, prediction=prediction, analysis=analysis)

@main_bp.route('/about')
def about():
    """Ruta para la página de información"""
    return render_template('about.html')

@main_bp.app_errorhandler(404)
def page_not_found(e):
    """Manejador para errores 404"""
    return render_template('404.html'), 404

@main_bp.app_errorhandler(500)
def internal_server_error(e):
    """Manejador para errores 500"""
    return render_template('500.html'), 500