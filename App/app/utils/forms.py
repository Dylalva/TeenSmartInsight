from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class PredictionForm(FlaskForm):
    """Formulario para recopilar datos para la predicción"""
    
    Daily_Usage_Hours = FloatField(
        'Horas de uso diario', 
        validators=[DataRequired(), NumberRange(min=0, max=24)],
        render_kw={"placeholder": "Ej: 5.5"}
    )
    
    Apps_Used_Daily = IntegerField(
        'Aplicaciones usadas diariamente',
        validators=[DataRequired(), NumberRange(min=0, max=100)],
        render_kw={"placeholder": "Ej: 8"}
    )
    
    Time_on_Social_Media = FloatField(
        'Tiempo en redes sociales (horas)',
        validators=[DataRequired(), NumberRange(min=0, max=24)],
        render_kw={"placeholder": "Ej: 2.5"}
    )
    
    Time_on_Gaming = FloatField(
        'Tiempo en juegos (horas)',
        validators=[DataRequired(), NumberRange(min=0, max=24)],
        render_kw={"placeholder": "Ej: 1.5"}
    )
    
    Phone_Checks_Per_Day = IntegerField(
        'Veces que revisa el teléfono al día',
        validators=[DataRequired(), NumberRange(min=0, max=1000)],
        render_kw={"placeholder": "Ej: 50"}
    )
    
    Sleep_Hours = FloatField(
        'Horas de sueño',
        validators=[DataRequired(), NumberRange(min=0, max=24)],
        render_kw={"placeholder": "Ej: 7.5"}
    )
    
    Weekend_Usage_Hours = FloatField(
        'Horas de uso en fin de semana',
        validators=[DataRequired(), NumberRange(min=0, max=48)],
        render_kw={"placeholder": "Ej: 8.0"}
    )
    
    Academic_Performance = FloatField(
        'Rendimiento académico (escala 1-10)',
        validators=[DataRequired(), NumberRange(min=1, max=10)],
        render_kw={"placeholder": "Ej: 7.5"}
    )
    
    submit = SubmitField('Analizar')