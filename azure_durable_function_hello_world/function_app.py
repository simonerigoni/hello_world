import azure.functions as func
import azure.durable_functions as dfunc

app = dfunc.DFApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# http://localhost:7071/api/orchestrators/hello_orchestrator

@app.route(route="orchestrators/{functionName}")
@app.durable_client_input(client_name="client")
async def http_start(req: func.HttpRequest, client):
    function_name = req.route_params.get('functionName')
    instance_id = await client.start_new(function_name)
    response = client.create_check_status_response(req, instance_id)
    return response

# Orchestrator
@app.orchestration_trigger(context_name="context")
def hello_orchestrator(context):
    result1 = yield context.call_activity("say_hello", "World")
    result2 = yield context.call_activity("say_hello", "World")

    return [result1, result2]

# Activity
@app.activity_trigger(input_name="name")
def say_hello(name: str):
    return f"Hello {name}!"
