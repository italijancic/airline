# Descrive the instrucción to create a docker image
FROM python:3
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD [ "python3", "manage.py", "runserver", "--settings=airline.settings.production", "0.0.0.0:8000" ]