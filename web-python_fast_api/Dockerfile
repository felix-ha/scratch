FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN pytest

WORKDIR /app/server

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
