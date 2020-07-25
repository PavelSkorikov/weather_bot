FROM python:3

RUN adduser --disabled-password --gecos "" app
USER app

WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/app/start.sh"]
