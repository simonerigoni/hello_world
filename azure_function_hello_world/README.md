# Azure Function Hello World

## Introduction

A simple Azure Function that return "Hello World!".

## Software and libraries

This project uses Python 3.11.9 and the most important packages are:

- [azure-functions](https://pypi.org/project/azure-functions/)

To create the virtual enviroment you can run `python -m venv .venv`.

To activate your newly created virtual enviroment run `.\.venv\Scripts\Activate.ps1`

To install the needed python packages you can run `pip install -r requirements.txt`.

## Local configuration

The `local.settings.json` file is a configuration file used in Azure Functions projects to define settings and environment variables for running your functions locally.

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "",
    "FUNCTIONS_WORKER_RUNTIME": "python"
  }
}
```

## Running the code

In VS Code if you have installed the Azure Functions Extension you can press F5 or alternatively you can run `.\.venv\Scripts\Activate.ps1; func start`. Now you can open your web browser and visit http://localhost:7071/api/http_trigger.

Note that the configuration of `.vscode/tasks.json` handles pip upgrade, pip install and func start.