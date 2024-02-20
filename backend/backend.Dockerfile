FROM python:3.11.5

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./health_patterns /code/health_patterns

CMD uvicorn health_patterns.main:app --host 0.0.0.0 --port 3000 --reload