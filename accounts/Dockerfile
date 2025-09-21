FROM python:3.13-alpine3.22

WORKDIR /accounts

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD /bin/sh -c ./start.sh