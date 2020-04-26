FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH /usr/src/app
WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock  ./
RUN pip install -U pip pipenv && pipenv install --system --deploy --ignore-pipfile --dev

COPY . .

RUN chmod 777 ./entry.sh

CMD ["./entry.sh"]