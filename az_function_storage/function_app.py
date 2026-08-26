import azure.functions as func
import datetime
import json
import logging
import os
from azure.storage.blob import BlobServiceClient

app = func.FunctionApp()

@app.route(route="StorageBlobFunction", auth_level=func.AuthLevel.ANONYMOUS)
def StorageBlobFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('StorageBlobFunction received a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = None
        if req_body:
            name = req_body.get('name')

    if not name:
        name = "anonymous"

    timestamp = datetime.datetime.utcnow().isoformat()
    record = {
        "name": name,
        "timestamp": timestamp
    }

    connection_string = os.environ["AzureWebJobsStorage"]
    container_name = "function-records"

    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    try:
        container_client.create_container()
    except Exception:
        pass

    blob_name = f"record-{timestamp}.json"
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(json.dumps(record), overwrite=True)

    return func.HttpResponse(
        json.dumps({
            "message": f"Hello, {name}. Your request was recorded in Azure Storage.",
            "blob_name": blob_name,
            "container": container_name
        }),
        mimetype="application/json",
        status_code=200
    )
