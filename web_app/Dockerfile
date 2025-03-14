FROM python:3.9
WORKDIR /app/web_app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "web_app.py"]