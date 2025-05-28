# Docker Client Server Hello World

## Introduction

A simple example of two Docker containers communicating. One container runs a Flask server and the other runs a client that sends requests to the server.

## Software and libraries

This project uses Python 3.11.9

To setup a new local enviroment and install all dependencies you can run `.\my_scripts\Set-Up.ps1`

Alternatively to create the virtual enviroment you can run `python -m venv .venv` in client and server folder.

More informations in `requirements.txt`. I am providing a simplified version of the file and letting pip handle the dependencies to avoid maintenance overhead.

To create a complete requirements file you can run `pip freeze > requirements.txt` and to install all python packages in it you can run `pip install -r requirements.txt`.

## Local configuration

The `.env` file is a configuration file used to define settings and environment variables for running the code locally.

```
SERVER_HOST=127.0.0.1
```

## Running the code

### Local

Open two different command line:

```
cd server
.\.venv\Scripts\Activate.ps1
python server.py
```

and

```
cd client
.\.venv\Scripts\Activate.ps1
python client.py
```

In the client you will see the answers from the server.

### Docker

Let's run `docker-compose up`. You will see that the images are build and the containsers executed.

[Running](images/running.JPG)

Then we can press CTRL+C to quit.