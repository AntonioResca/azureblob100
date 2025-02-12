import azure.functions as func
import logging
from blobfun import blob as blob

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="write_blob")
def write_blob(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        blob.write_blob_to_storage(req_body)
        return func.HttpResponse(f"Hello, {name}. Your name is now written in Azure Storage")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.route(route="read_blob")
def read_blob(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(f"Hello, {blob.read_blob_from_storage()}. I read your name in Azure Storage")