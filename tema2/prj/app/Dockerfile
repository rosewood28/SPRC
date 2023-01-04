FROM python:3.8

#install psycopg2
RUN pip install --upgrade pip
RUN apt-get update
RUN pip install psycopg2


RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]