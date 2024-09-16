# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set environment variables to prevent bytecode generation and buffer I/O
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project to the container
COPY . /app/

# Expose port 8000 to access the Django app
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

