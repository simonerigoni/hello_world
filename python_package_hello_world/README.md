# Python Package Hello World

## Introduction

A simple Hello World Python package. It shows how to structure, build and install a package with a command line entry point.

## Software and libraries

This project uses Python 3.11 and [uv](https://docs.astral.sh/uv/) with the `uv_build` build backend. It has no dependencies.

## Running the code

### Run

From this folder, run `uv run python-package-hello-world` or `uv run python -m python_package_hello_world`. You will see the message `Hello World!`.

### Build

Run `uv build` to create the source distribution and the wheel in the `dist` folder.

### Install

Install the wheel in any environment with `pip install dist/python_package_hello_world-0.1.0-py3-none-any.whl`, then run `python-package-hello-world`.
