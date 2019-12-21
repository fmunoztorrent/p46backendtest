FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /p46test
WORKDIR /p46test
ADD requirements.txt /p46test/
RUN pip install -r requirements.txt
ADD . /p46test/