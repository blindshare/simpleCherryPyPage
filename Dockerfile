FROM alpine:edge

RUN  echo "http://dl-3.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories
RUN  echo "http://dl-3.alpinelinux.org/alpine/edge/community/" >> /etc/apk/repositories
RUN  apk -U upgrade 
RUN  apk add py3-pip
RUN  pip3 install cherrypy

RUN  mkdir /opt/simpleTest
COPY simple.py /opt/simpleTest

CMD ["/usr/bin/python3", "/opt/simpleTest/simple.py"]
