FROM python:3.11.0

COPY requirements.txt .

RUN pip3 install --upgrade pip -r requirements.txt

COPY src /backend/src

WORKDIR /backend/src

EXPOSE 5000

COPY model /backend/model/

COPY token /backend/token/

CMD ["flask", "--app",  "main", "run", "--host=0.0.0.0"]
