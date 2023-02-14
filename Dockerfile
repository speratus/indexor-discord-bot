FROM python:alpine3.16

RUN apk add git

ENV DISCORD_TOKEN=""

COPY . /opt/dewey/
WORKDIR /opt/dewey/


RUN pip install -r /opt/dewey/requirements.txt

CMD python indexor_discord_bot