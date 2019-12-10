FROM python:3.8.0-slim-buster

WORKDIR /ebook_automation

RUN apt-get update && \
    apt-get install -y git libsaxonb-java python3-bs4

RUN rm -rf /var/cache/apt/*

RUN git clone https://github.com/OpenBookPublishers/XML-last.git

COPY run ./
COPY ./src/ ./src/

CMD bash run epub_file
