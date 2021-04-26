from alpine:latest

RUN apk add --no-cache python3-dev \
    && apk add --update py3-pip \
    && apk update \
    && apk add alpine-sdk gcc musl-dev python3-dev libffi-dev openssl-dev cargo\
    && pip3 install --upgrade pip 

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt 

ENTRYPOINT ["python3"]
CMD ["app.py"]
