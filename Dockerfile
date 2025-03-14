# Use the official Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /habitTracker

# Copy the requirements file first to avoid reinstalling packages on every change
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port Django runs on
EXPOSE 8000

# Run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
