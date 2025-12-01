FROM python:3.10-slim

# Install system deps
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install requirements
RUN pip install --no-cache-dir torch==2.0.1 --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir sentence-transformers fastapi uvicorn

# Copy your app
WORKDIR /app
COPY . /app

# Expose port (Railway expects 8000)
EXPOSE 8000

# Run API on port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


