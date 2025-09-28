FROM python:3.13-alpine3.22

ENV PYTHONUNBUFFERED 1

WORKDIR /blog

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8001"]