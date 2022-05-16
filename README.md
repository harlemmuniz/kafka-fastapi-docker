# kafka-fastapi-docker
A FastAPI and Apache Kafka project built in a Docker container

## 💻 Requirements

First of all, you need to configure your enviroment:

* Python `3.9` installed
* Pip `3` installed
* Java `8` installed
* Docker installed
* Docker-compose installed

## 📫 Pull or clone the kafka-fastapi-docker
1. ```git init```
2. ```git remote add origin https://github.com/harlemmuniz/kafka-fastapi-docker.git```
3. ```git pull origin main```

or

1. ```git init```
2. ```git clone https://github.com/harlemmuniz/kafka-fastapi-docker.git```

## 🚀 Installing and configuringkafka-fastapi-docker

Installing Kafka and Kafdrop using docker compose in project/kafka folder:

```cd /path/to/root/project/kafka```

```docker-compose up -d```

Installing a Python virtual environment:

```pip3 install virtualenv```

Creating a Python virtual environment in the project root folder:

```cd /path/to/root/project```

```virtualenv env```

Activating the virtual environment:

```source env/bin/activate```

Installing the required libraries:

```pip3 install fastapi aiokafka uvicorn```

Starting the application:

```uvicorn main:app --reload```

If you want to run the project in a Google Cloud, you will need to install the gunicorn:

```pip3 install gunicorn```
