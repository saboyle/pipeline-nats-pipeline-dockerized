# pipeline-nats-pipeline-dockerized

**Status** [DEV/ALPHA - Exploration only]

Sample dockerized pipeline

``` bash
# Upgrading Pip
pip install --upgrade pip

# Installing Requirements
pip install asyncio-nats-client

# Freezing requirements
pip freeze > requirements.txt

# Building docker file
docker build -t python-nats-pipeline

# Running docker pipeline with NATS docker image
???
```

## Refs
* https://stackabuse.com/dockerizing-python-applications/
* https://runnable.com/docker/python/dockerize-your-python-application