# Docker Hello World

## Introduction

A simple Hello World python script that also print the current OS and architecture.

## Software and libraries

This project uses Python 3.11.9

## Running the code

First let's build the docker image by runing `docker build -t my-python-image .`

If you run `python docker_hello_world.py` you will see the message and your current OS and architecture while if you run `docker run -v .:/app my-python-image` you will see the message and image's OS and architecture.
