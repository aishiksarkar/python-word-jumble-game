FROM alpine

RUN apk add --update --no-cache python3
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

WORKDIR /usr/app

COPY ./ ./

CMD ["python","wordgameoops.py"]