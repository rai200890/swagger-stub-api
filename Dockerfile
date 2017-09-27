FROM ubuntu:xenial
WORKDIR /code
RUN apt-get -qq update && apt-get install -y git ca-certificates python-dev python3-pip python3
RUN pip3 install --upgrade pip
ADD requirements.txt requirements-dev.txt /code/
RUN pip3 install -r requirements-dev.txt
