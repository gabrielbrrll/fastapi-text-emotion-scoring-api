FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY emotion_service.py .

CMD ["uvicorn", "emotion_service:app", "--host", "0.0.0.0", "--port", "8000"]
