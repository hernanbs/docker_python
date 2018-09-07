FROM ubuntu:16.04
LABEL maintainer="Hernan Santos"
LABEL version="1.0"

WORKDIR /home/

#Mudando data e hora
RUN apt -y update && apt install -y tzdata
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo $TZ > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata  && date
#
RUN apt -y update && apt install -y  python3 python3-pip  gdal-bin postgis
RUN pip3 install --upgrade pip
RUN pip3 install psycopg2-binary
RUN pip3 install requests
COPY ./python-script/ /home/
#CMD python3 -u main.py


