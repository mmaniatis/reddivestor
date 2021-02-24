FROM python:3.8.5

COPY . /app

# RUN pip install -r requirements.txt

CMD ["ls"]

CMD ["python3", "/app/main.py"]

