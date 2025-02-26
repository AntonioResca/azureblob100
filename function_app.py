import azure.functions as func
import logging
from blobfun import blob as blob

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="write_blob")
def write_blob(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    blob.write_blob_to_storage(req_body)
    return func.HttpResponse(
            "Success!",
            status_code=200
    )

@app.route(route="write_json")
def write_json(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    myData = {
        "avalancheProblems" : [ {
        "problemType" : "wind_slab",
        "elevation" : {
            "lowerBound" : "treeline"
        },
        "validTimePeriod" : "all_day",
        "snowpackStability" : "poor",
        "frequency" : "some",
        "avalancheSize" : 2,
        "customData" : {
            "ALBINA" : {
            "avalancheType" : "slab"
            }
        },
        "aspects" : [ "W", "NE", "SE", "S", "E", "N", "SW", "NW" ]
        },{
        "problemType" : "persistent_weak_layers",
        "elevation" : {
            "lowerBound" : "2400"
        },
        "validTimePeriod" : "all_day",
        "snowpackStability" : "poor",
        "frequency" : "few",
        "avalancheSize" : 2,
        "customData" : {
            "ALBINA" : {
            "avalancheType" : "slab"
            }
        },
        "aspects" : [ "W", "NE", "E", "N", "NW" ]
        } ]
    }
    blob.write_json_to_storage(myData)
    return func.HttpResponse(
            "Success!",
            status_code=200
    )

@app.route(route="read_blob")
def read_blob(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(f"Hello, {blob.read_blob_from_storage()}. I read your name in Azure Storage")