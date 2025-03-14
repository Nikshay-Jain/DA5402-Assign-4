# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app/rss_reader

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY . .

# Run the RSS reader script
CMD ["python", "rss_reader.py"]
