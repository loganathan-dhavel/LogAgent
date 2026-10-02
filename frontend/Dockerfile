FROM python:3.14-slim
WORKDIR /app
RUN pip install --no-cache-dir streamlit dotenv
COPY frontend/ .
CMD ["streamlit", "run", "streamlit_app.py"]