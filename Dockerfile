FROM python:3.6

RUN apt-get update -y && apt-get install -y git build-essential unzip zip

RUN pip install antlr4-python3-runtime

ADD . /beta
RUN cd /beta && pip install .
