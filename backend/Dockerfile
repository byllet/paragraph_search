FROM python:3.11.0

WORKDIR /backend

COPY requirements.txt .

RUN pip3 install --upgrade pip -r requirements.txt

COPY src /backend/src

WORKDIR /backend/src

EXPOSE 5000

CMD ["flask", "--app",  "backend", "run", "--host=0.0.0.0"]
