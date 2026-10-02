FROM python:3.14-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY api/ .
EXPOSE 8000
EXPOSE 11434
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]