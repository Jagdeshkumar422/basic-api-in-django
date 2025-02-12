# Use official Python image as base
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy requirements file first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the port Django will run on
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
