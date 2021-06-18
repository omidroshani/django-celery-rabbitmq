FROM ubuntu:latest


RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

ENV TZ=Asia/Tehran
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# set work directory
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONWARNINGS "ignore:Unverified HTTPS request"

# install psycopg2 dependencies
RUN apt-get update && apt-get install -y libpq-dev

# install requirements
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# copy project
WORKDIR /core
COPY ./core /core
