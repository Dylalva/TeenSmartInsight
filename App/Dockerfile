FROM python:3.10-slim

WORKDIR /app

# Copiar los archivos de requisitos primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Crear directorio para datos si no existe
RUN mkdir -p data

# Exponer el puerto que usa la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "run.py"]