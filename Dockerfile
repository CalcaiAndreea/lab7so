# Etapa 1: Construirea imaginii de bază
FROM python:3.11-slim AS build

# Setăm directorul de lucru
WORKDIR /app

# Instalăm dependențele
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiem restul codului sursă
COPY app.py .
COPY templates/ templates/

# Etapa 2: Crearea imaginii finale
FROM python:3.11-slim

# Setăm directorul de lucru
WORKDIR /app

# Instalăm dependențele runtime
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /app /app

# Expunem portul
EXPOSE 8080

# Comanda de start
CMD ["python", "app.py"]
