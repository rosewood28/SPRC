FROM python:3.8

RUN pip install --upgrade pip
RUN apt-get update

RUN mkdir /adapterMQTT-DB
WORKDIR /adapterMQTT-DB
COPY . /adapterMQTT-DB
RUN pip install --no-cache-dir -r requirements.txt

RUN sleep 3

CMD ["python3", "-u", "adapter.py"]
