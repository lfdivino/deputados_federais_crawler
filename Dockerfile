FROM alpine:3.6

MAINTAINER Luiz Felipe do Divino "lf.divino@gmail.com"

RUN apk add --update \
    python3 \
    py-pip \
    py-setuptools \
    python-dev \
    python3-dev \
    libffi-dev \
    build-base \
    alpine-sdk \
    openssl-dev \
    libxslt-dev \
  && pip install flask -U \
  && pip install incremental -U \
  && rm -rf /var/cache/apk/* \
  && adduser -D app \
  && mkdir /foo  \
  && chown -R app:app /foo

USER root

ADD api.py /foo/api.py
ADD requirements.txt /foo/requirements.txt
ADD deputados_api/ /foo/deputados_api
ADD deputados_federais_crawler/ /foo/deputados_federais_crawler

RUN pip3 install -r /foo/requirements.txt

CMD python3 /foo/api.py