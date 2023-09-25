# backend Dockerfile

FROM python:3

WORKDIR /aid_vault

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY aid_vault/ ./

EXPOSE 5000

CMD ["flask", "run", "--debug", "--host=0.0.0.0"]