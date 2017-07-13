# Audio Labeling Container
FROM ubuntu:14.04

MAINTAINER Steve McLaughlin <stephen.mclaughlin@utexas.edu>

EXPOSE 8881
EXPOSE 27017

ENV SHELL /bin/bash
ENV PYTHONWARNINGS="ignore:a true SSLContext object"

# Update OS
RUN apt-get update && apt-get install -y \
software-properties-common \
build-essential \
python-dev \
python-pip \
wget \
git \
unzip \
dpkg \
gunicorn \
libxml2-dev \
libxslt1-dev \
libssl-dev \
&& python -m pip install -U pip

COPY ./setup.sh /var/local/

COPY ./requirements.txt /var/local/
RUN pip install -qr /var/local/requirements.txt

#RUN mkdir -p /home/static/
#COPY ./static/ /home/static/

#RUN mkdir -p /home/templates/
#COPY ./templates/ /home/templates/

#COPY ./app.py /home/
#COPY ./wsgi.py /home/
COPY ./load_metadata_db.py /home/


WORKDIR /home/
#CMD ["bash","/var/local/setup.sh"]
