FROM python:alpine3.16

RUN apk add git

ENV DISCORD_TOKEN=""
ENV ENGINE_URL="http://localhost:8000"

COPY . /opt/casper/
WORKDIR /opt/casper/


RUN pip install -r /opt/casper/requirements.txt

CMD python indexor_discord_bot