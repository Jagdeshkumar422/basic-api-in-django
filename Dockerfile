# Use official Python image as base
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary

# Expose port
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
