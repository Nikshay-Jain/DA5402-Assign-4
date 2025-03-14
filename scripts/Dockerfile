# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY rss_reader.py rss_reader.py

# Run the RSS reader script
CMD ["python", "rss_reader.py"]