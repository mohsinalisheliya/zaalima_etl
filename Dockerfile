FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
#add the values of your AWS access key and secret access key here
ENV AWS_ACCESS_KEY_ID="placeholder"
ENV AWS_SECRET_ACCESS_KEY="placeholder" 
ENV S3_BUCKET_NAME="zaalima-data-lake"

COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]