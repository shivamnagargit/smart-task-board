# Use official Python image
FROM python:3.10-slim

# Set the working directory inside the box
WORKDIR /app

# Copy the tools list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your actual Python code
COPY . .

# Open port 8000
EXPOSE 8000

# The command to turn on the Kitchen
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
