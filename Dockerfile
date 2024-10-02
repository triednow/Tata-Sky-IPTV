FROM python:3.9


WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app
COPY . . 

RUN pip3 install -r requirements.txt 

CMD ["bash","start.sh"]
