FROM python:3.10-slim-bullseye

WORKDIR /usr/src/adistetsa

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/adistetsa/entrypoint.sh
RUN chmod +x /usr/src/adistetsa/entrypoint.sh

COPY . .