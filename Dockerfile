FROM daocloud.io/python:3.6
MAINTAINER shippo <shipporun@gmail.com>

COPY . /docker
WORKDIR /docker

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python3", "./app/init.py"]
