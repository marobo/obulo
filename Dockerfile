FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 🔥 Copy ONLY requirements first (important!)
COPY requirements.txt .

# Install Python dependencies (cached layer)
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your app
COPY . .

# Make entrypoint executable
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "obulo.wsgi:application"]