# 1. Pornim de la o imagine oficiala si usoara de Python
FROM python:3.12-slim

# 2. Setam directorul de lucru in interiorul containerului
WORKDIR /app

# 3. Copiem fisierul cu dependente in container
COPY requirements.txt .

# 4. Instalam biblioteca 'requests' (si altele daca ai) in container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiem restul codului sursa (adica scriptul weather.py) in container
COPY . .

# 6. Comanda care se va executa automat cand porneste containerul
CMD ["python", "weather.py"]
