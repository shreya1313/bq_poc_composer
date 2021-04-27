from alpine:latest

RUN apk add --no-cache python3-dev \
    && apk add --update py3-pip \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

ENTRYPOINT ["python3"]
CMD ["demo.py"]
