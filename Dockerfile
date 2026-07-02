FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV AWS_ACCESS_KEY_ID="placeholder"
ENV AWS_SECRET_ACCESS_KEY="placeholder"
ENV S3_BUCKET_NAME="zaalima-data-lake"
CMD ["python", "main.py"]