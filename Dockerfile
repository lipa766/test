FROM python:3.9-slim-buster

WORKDIR /app/

COPY Pipfile* /app/

RUN pip install pipenv && pipenv install

COPY . .

EXPOSE 5010

CMD ["python", "app.py"]