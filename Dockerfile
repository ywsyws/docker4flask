# Download base image ubuntu 18.04
FROM ubuntu:18.04

# Label the docker image
LABEL maintainer="yws <channing.platevoet@gmail.com>" version="1.0"

# Update Ubuntu Software repository and install Python, pip & git from Ubuntu software repository
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev && \
    apt-get install -y git

# Configure git account
RUN git config --global user.name "ywsyws" && \
    git config --global user.email "channing.platevoet@gmail.com" && \
    git config --global credential.helper store

# Create a work directory
RUN mkdir /app

# Set work directory
WORKDIR /app

# Copy the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Create a virtual environment and activate it
RUN python3 -m venv venv && \
    source venv/bin/activate

# Install all the required libraries in the virutal environment created
RUN venv/bin/pip3 install -r requirements.txt

# Copy the local working directory to docker
COPY . .

# Crate a volume
VOLUME [ "/app" ]

# Set FLASK_APP to hello.py
ENV FLASK_APP=hello.py FLASK_DEBUG=1

# Define the port
EXPOSE 5000

# Set the default command that will be ran when the docker image gets started
CMD flask run --host=0.0.0.0 --port=5000