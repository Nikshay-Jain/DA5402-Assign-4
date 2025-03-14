# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app/web_app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application and templates
COPY . .

# Run the web app
CMD ["python", "web_app.py"]