FROM python:3.10

WORKDIR /app
COPY ./app /app/`
COPY ./entrypoint.sh .
COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "sh", "preStart.sh" ]