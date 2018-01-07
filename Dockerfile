FROM python:3.6

MAINTAINER Max Kotov <maxkotovfromrussia@gmail.com>

EXPOSE 5000

ADD . /src

WORKDIR /code

RUN pip install -r 'requirements.txt'

CMD python app.py