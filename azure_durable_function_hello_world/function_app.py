import azure.functions as func
import azure.durable_functions as dfunc
import json
import logging

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
    result1 = yield context.call_activity("say_hello", "World")
    result2 = yield context.call_activity("say_hello", "World")
    logging.info(f"Orchestration ended.")
    return [result1, result2]

# Activity
@app.activity_trigger(input_name="name")
def say_hello(name: str):
    return f"Hello {name}!"
