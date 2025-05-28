import azure.functions as func
import azure.durable_functions as dfunc
import json
import logging
import os
import platform

ENV = os.getenv("ENV")

app = dfunc.DFApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# http://localhost:7071/api/orchestrators/hello_orchestrator

@app.route(route="orchestrators/{functionName}")
@app.durable_client_input(client_name="client")
async def http_start(req: func.HttpRequest, client):
    function_name = req.route_params.get('functionName')
    instance_id = await client.start_new(function_name)
    logging.info(f"From http_start started orchestration with ID = '{instance_id}'.")
    response = client.create_check_status_response(req, instance_id)
    response_body = response.get_body().decode('utf-8')
    response_json = json.loads(response_body)
    status_query_uri = response_json.get("statusQueryGetUri")
    logging.info(f"Status query url: {status_query_uri}.")
    return response

# Orchestrator
@app.orchestration_trigger(context_name="context")
def hello_orchestrator(context):
    result = yield context.call_activity("say_hello")
    logging.info(f"Orchestration ended.")
    return result

# Activity
@app.activity_trigger(input_name="payload")
def say_hello(payload: dict):
    os_name = platform.system()
    architecture = platform.architecture()
    return f"Hello World! from {os_name} operating system on {architecture[0]} {architecture[1]} architecture in {ENV} enviroment"
