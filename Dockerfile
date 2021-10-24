FROM python:3.7

RUN mkdir /app
COPY /smashed-it-test-app /app
COPY pyproject.toml /app
WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV FLASK_APP=smash_it_container/app.py
ENV FLASK_ENV=production

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

RUN flask run
