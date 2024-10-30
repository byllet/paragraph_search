FROM python:3.11.0

COPY requirements.txt .

RUN pip3 install --upgrade pip -r requirements.txt

EXPOSE 5000

RUN python -c 'from sentence_transformers import SentenceTransformer; embedder = SentenceTransformer("intfloat/multilingual-e5-large")'

COPY src /backend/src

WORKDIR /backend/src

CMD ["flask", "--app",  "main", "run", "--host=0.0.0.0"]
