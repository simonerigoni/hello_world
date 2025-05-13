# Docker Hello World

## Introduction

A simple Hello World python script that also print the current OS and architecture.

## Software and libraries

This project uses Python 3.11.9

## Running the code

### Local

You can run the script with the command `python docker_hello_world.py`. You will see the message and your current OS and architecture.

### Docker

First let's build the docker image by runing `docker build --tag my-python-image:v1.0.0 .`

Then if you run `docker run -v .:/app my-python-image:v1.0.0` you will see the message and the image's OS and architecture.
