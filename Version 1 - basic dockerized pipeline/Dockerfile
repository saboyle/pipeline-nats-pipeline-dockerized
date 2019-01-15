FROM python:3.7-alpine

COPY ./pipeline.py /
COPY ./requirements.txt /

WORKDIR /

RUN pip install -r requirements.txt

CMD ["python", "./pipeline.py"]