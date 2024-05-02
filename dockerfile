FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir Flask

EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
