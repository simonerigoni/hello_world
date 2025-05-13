import platform
import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# http://localhost:7071/api/http_trigger

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(f"From http_trigger started execution.")
    os_name = platform.system()
    architecture = platform.architecture()
    return func.HttpResponse(f"Hello World! from {os_name} operating system on {architecture[0]} {architecture[1]} architecture", status_code = 200)