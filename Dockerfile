# Use a specific Python version as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Define the entry point
ENTRYPOINT ["python", "app.py"]
