FROM python:3.11

WORKDIR /app
COPY ./app /app/app
COPY ./preStart.sh .
COPY ./alembic.ini .
COPY ./requirements.txt .
RUN chmod +x preStart.sh
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "sh", "preStart.sh" ]