FROM python:3.14-slim
WORKDIR /app
RUN pip install --no-cache-dir streamlit dotenv
COPY api/ .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]