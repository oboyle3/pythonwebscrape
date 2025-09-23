# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Run Django on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
