FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

ADD . /tancho/
ADD requirements.txt /tancho/
WORKDIR /tancho

RUN pip install -r requirements.txt
