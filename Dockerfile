FROM python:3.8.0-slim-buster

ENV XML_LAST_VERSION=0.0.2

WORKDIR /ebook_automation

# https://github.com/geerlingguy/ansible-role-java/issues/64#issuecomment-393299088
RUN mkdir -p /usr/share/man/man1
RUN apt-get update && \
    apt-get install -y git openjdk-11-jdk libsaxonb-java zip
RUN rm -rf /var/cache/apt/*

ADD https://github.com/OpenBookPublishers/XML-last/archive/${XML_LAST_VERSION}.zip /tmp/.
RUN unzip /tmp/${XML_LAST_VERSION}.zip -d ./
RUN mv XML-last-${XML_LAST_VERSION} XML-last

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY run ./
COPY ./src/ ./src/

ENV OUTDIR=/ebook_automation/output

CMD bash run epub_file
