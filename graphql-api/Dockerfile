FROM python:3.9

ARG DB_HOST
ENV MONGO_HOST ${DB_HOST}

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
