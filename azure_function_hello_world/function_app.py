import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level = func.AuthLevel.ANONYMOUS)

# http://localhost:7071/api/http_trigger

@app.route(route = "http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"From http_trigger started execution.")
    return func.HttpResponse("Hello World!", status_code = 200)