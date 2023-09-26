FROM python:3.11.5

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./aid_vault /code/aid_vault

CMD uvicorn aid_vault.main:app --host 0.0.0.0 --port 5000 --reload