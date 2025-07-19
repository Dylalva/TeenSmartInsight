from markupsafe import Markup

def nl2br(value):
    """Convierte saltos de línea en etiquetas <br>"""
    if not value:
        return ""
    return Markup(value.replace('\n', '<br>'))