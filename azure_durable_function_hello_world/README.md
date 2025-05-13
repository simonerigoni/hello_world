# Azure Durable Function Hello World

## Introduction

A simple Azure Durable Function that says "Hello World!". Durable Functions is an extension of Azure Functions that enable us to write stateful functions in a serverless compute environment. The extension lets you define stateful workflows by writing orchestrator functions and stateful functions. Basically the extension manages state, checkpoints, and restarts for you, allowing you to focus on your business logic. This is done by leveraging the [Durable Task Framework (DTFx)](https://github.com/Azure/durabletask).

Durable Functions requires an Azure storage account to run because it uses the storage account to manage state, queues, and other runtime data necessary for orchestrating and executing long-running workflows. You can choose to:

1. Create a storage account on Azure
2. Use [Azurite](https://github.com/Azure/Azurite)

In this example I will use Azurite which is an open-source emulator provides a free local environment for testing your Azure Blob, Queue Storage, and Table Storage applications. 

To install it you can run `npm install -g azurite`.

## Software and libraries

This project uses Python 3.11.9 and the most important packages are:

- [azure-functions](https://pypi.org/project/azure-functions/)
- [azure-functions-durable](https://pypi.org/project/azure-functions-durable/)

To create the virtual enviroment you can run `python -m venv .venv`.

To activate your newly created virtual enviroment run `.\.venv\Scripts\Activate.ps1`

To install the needed python packages you can run `pip install -r requirements.txt`.

## Local configuration

The `local.settings.json` file is a configuration file used in Azure Functions projects to define settings and environment variables for running your functions locally.

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsFeatureFlags": "EnableWorkerIndexing"
  }
}
```

Note the `"AzureWebJobsStorage": "UseDevelopmentStorage=true"` that tells Azure Functions Core Tools to use the Azurite emulator.

## Running the code 

In VS Code if you have installed the Azure Functions Extension you can press F5. Now you can open your web browser and visit http://localhost:7071/api/orchestrators/hello_orchestrator. This will start the execution of a new instance of the specified orchestrator function. The response payload is a JSON object with some fields: one of which is `statusQueryGetUri. This field is the status URL of the orchestration instance and if you visit it you will see something like this:

```json
{"name":"hello_orchestrator","instanceId":"...","runtimeStatus":"Completed","input":null,"customStatus":null,"output":["Hello World!","Hello World!"],"createdTime":"...","lastUpdatedTime":"..."}
```

Note that the configuration of `.vscode/tasks.json` handles pip upgrade, pip install, starting azurite and func start.