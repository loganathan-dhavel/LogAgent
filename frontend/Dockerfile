FROM python:3.14-slim
WORKDIR /app
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir streamlit dotenv
COPY frontend/ .
EXPOSE 8501
EXPOSE 8000
CMD ["streamlit", "run", "streamlit_app.py"]