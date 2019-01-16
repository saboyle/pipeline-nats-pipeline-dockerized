# Version 1

## To run example

* CD to directory
* Run 3 terminals:

Terminal 1: Runs the Dockerized pipeline
``` bash
# To build the pipeline docker image
docker-compose build

# To run the pipeline & single NATS server
docker-compose up
```
Terminal 2: Runs a wiretap on the output message queue
``` bash
python nats-wiretap p1.s3
```

Terminal 3: Generates test messages and sends to input queue.
``` bash
python client.py
```

The configuration of the Dockerized pipeline is defined in the docker-compose.yml file:

``` yaml
version: '0.1'

services:

  nats:
      image: nats:latest
      ports:
      - "4222:4222"
      - "6222:6222"
      - "8222:8222"

  pipeline:
    build: .
    links:
      - nats

```

The DockerFile for the pipeline service:

``` Dockerfile
FROM python:3.7-alpine

COPY ./pipeline.py /
COPY ./requirements.txt /

WORKDIR /

RUN pip install -r requirements.txt

CMD ["python", "./pipeline.py"]

```