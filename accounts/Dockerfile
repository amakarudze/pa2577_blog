FROM python:3.13-alpine3.22

ENV PYTHONUNBUFFERED 1

WORKDIR /accounts

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "accounts.wsgi:application", "--bind", "0.0.0.0:8000"]