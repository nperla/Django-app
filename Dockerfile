FROM python:3.9-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /app/script.sh

CMD ["./script.sh"]
