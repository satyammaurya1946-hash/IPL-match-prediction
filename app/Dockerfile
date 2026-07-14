FROM python:3.13.3-slim
RUN apt-get update && apt-get install -y gcc
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]