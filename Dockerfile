FROM python:3.12.0b1-slim

RUN mkdir /app
COPY /smashed_it_test_app /app
WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV FLASK_APP=smashed_it_test_app/app.py
ENV FLASK_ENV=production

RUN pip3 install -r requirements.txt

EXPOSE 5000

# test server only accessible locally
# --host-0.0.0.0 allows public access
ENTRYPOINT [ "flask", "run" , "--host=0.0.0.0"]
