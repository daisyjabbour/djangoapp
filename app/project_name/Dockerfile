# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install Django==2.2.5
RUN pip install psycopg2-binary==2.9.1
RUN pip install uvicorn
RUN pip install daphne 
RUN pip install gunicorn==21.2.0


# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000 for the Django application
EXPOSE 8000


