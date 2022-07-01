FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./start-api /start-api
RUN sed -i 's/\r//' /start-api
RUN chmod +x /start-api

COPY . /code/