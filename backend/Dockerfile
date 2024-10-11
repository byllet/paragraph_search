FROM python:3.11.0

WORKDIR /backend

COPY src /backend/src
COPY requirements.txt .

RUN pip3 install --upgrade pip -r requirements.txt

WORKDIR /backend/src

EXPOSE 5000

CMD ["flask", "--app",  "backend", "run"]