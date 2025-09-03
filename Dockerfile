# PARENT IMAGE
FROM python:3.10-slim

# ENV VARIABLES
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# WORK DIRECTORY
WORKDIR /app

## INSTALL SYSTEM DEPENDENCIES
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# COPY DIRECTORY
COPY . .

## RUN setup
RUN pip install --no-cache-dir -e .

#PORT
EXPOSE 8501


# RUN THE APP
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0","--server.headless=true"]
