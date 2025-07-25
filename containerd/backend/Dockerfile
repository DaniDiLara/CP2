# Usa imagen ligera con Python
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

# Asegura que el directorio de datos exista
RUN mkdir -p /mnt/data

# Expone el puerto de Flask
EXPOSE 5000

# Comando para lanzar la aplicación
CMD ["python", "app.py"]

