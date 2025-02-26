import azure.functions as func
import logging
from blobfun import blob as blob
import json
import csv
import io

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

@app.route(route="write_csv")
def write_csv(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    myData = [
        {"nome": "Luigi", "cognome": "Mazzini", "citta": "Napoli"},
        {"nome": "Marinella", "cognome": "Selva", "citta": "Torino"},
        {"nome": "Ciro", "cognome": "Iaccarino", "citta": "Napoli"},
        {"nome": "Claudio", "cognome": "Cibrabrio", "citta": "Ancona"}
    ]
    blob.write_csv_to_storage(myData)
    return func.HttpResponse(
            "Success!",
            status_code=200
    )

@app.route(route="read_blob")
def read_blob(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.HttpResponse(f"Hello, {blob.read_blob_from_storage()}. I read your name in Azure Storage")


@app.route(route="read_json")
def read_json(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    json_data = json.dumps(blob.read_json_from_storage())
    
    # Crea la response HTTP con il tipo di contenuto "application/json"
    return func.HttpResponse(
        body=json_data,
        status_code=200,
        mimetype="application/json",
        charset="utf-8"
    )

@app.route(route="read_csv")
def read_csv(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    csv_data = blob.read_csv_from_storage()

    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=csv_data[0].keys())
    
    writer.writeheader()
    writer.writerows(csv_data)
    csv_content = output.getvalue()
    
    # Crea la response HTTP con il tipo di contenuto "application/json"
    return func.HttpResponse(
        csv_content,
        status_code=200,
        mimetype="text/csv",
        charset="utf-8",
        headers={
            "Content-Disposition": 'attachment; filename="data.csv"'
        }
    )