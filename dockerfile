FROM python:3.11

WORKDIR /app

COPY . /app

#--> Install system dependencies (ffmpeg)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

#--> Expose the default Streamlit port
EXPOSE 8501

#--> Set environment variables to avoid Streamlit warnings
ENV PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ENABLECORS=false

CMD ["streamlit", "run", "app.py"]