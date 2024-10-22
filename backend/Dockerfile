# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Flask is running on
EXPOSE 5000

# Set environment variables
ENV FLASK_ENV=development

# Command to run the Flask app
CMD ["python", "app.py"]
