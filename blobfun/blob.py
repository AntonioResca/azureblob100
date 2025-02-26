import os
import io
import json
import csv
import pandas as pd 
import logging
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def write_blob_to_storage(req_body):
    try:
        # Retrieve connection string from environment variable
        connection_string = os.environ["AzureWebJobsStorage"]
        
        # Initialize BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Define container name and blob name
        container_name = "mycontainer"
        blob_name = "example.txt"
        
        # Create container if it doesn't exist
        container_client = blob_service_client.get_container_client(container_name)
        if not container_client.exists():
            container_client.create_container()

        # Define the content to upload
        content = req_body.get("name", "Default name")

        # Upload the content to the blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.upload_blob(content, overwrite=True)

        logging.info(f"Blob '{blob_name}' uploaded successfully.")
        return f"Blob '{blob_name}' uploaded successfully."

    except Exception as e:
        logging.error(f"Error uploading blob: {e}")
        return str(e)

def write_json_to_storage(mydict):
    try:
        # Retrieve connection string from environment variable
        connection_string = os.environ["AzureWebJobsStorage"]
        
        # Initialize BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Define container name and blob name
        container_name = "mycontainer"
        blob_name = "example.json"
        
        # Create container if it doesn't exist
        container_client = blob_service_client.get_container_client(container_name)
        if not container_client.exists():
            container_client.create_container()

        # convert dictionary to json
        myjson = json.dumps(mydict)
        # Upload json to blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.upload_blob(myjson, overwrite=True)

        logging.info(f"Blob '{blob_name}' uploaded successfully.")
        return f"Blob '{blob_name}' uploaded successfully."

    except Exception as e:
        logging.error(f"Error uploading blob: {e}")
        return str(e)
    

def write_csv_to_storage(mydict):
    try:
        # Retrieve connection string from environment variable
        connection_string = os.environ["AzureWebJobsStorage"]
        
        # Initialize BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Define container name and blob name
        container_name = "mycontainer"
        blob_name = "example.csv"
        
        # Create container if it doesn't exist
        container_client = blob_service_client.get_container_client(container_name)
        if not container_client.exists():
            container_client.create_container()

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=mydict[0].keys())
        writer.writeheader()
        writer.writerows(mydict)
        
        # Ottieni i dati CSV come stringa
        csv_data = output.getvalue()
        # Upload json to blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.upload_blob(csv_data, overwrite=True)

        logging.info(f"Blob '{blob_name}' uploaded successfully.")
        return f"Blob '{blob_name}' uploaded successfully."

    except Exception as e:
        logging.error(f"Error uploading blob: {e}")
        return str(e)


def read_json_from_storage():
    try:
        # Retrieve connection string from environment variable
        connection_string = os.environ["AzureWebJobsStorage"]
        
        # Initialize BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Define container name and blob name
        container_name = "mycontainer"
        blob_name = "example.json"

        # Get the blob client
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # Check if the blob exists
        if blob_client.exists():
            json_data = blob_client.download_blob().content_as_text() 
            logging.info(f"Blob '{blob_name}' read successfully.")
            return  json.loads(json_data)
        else:
            logging.warning(f"Blob '{blob_name}' does not exist.")
            return f"Blob '{blob_name}' does not exist."

    except Exception as e:
        logging.error(f"Error reading blob: {e}")
        return str(e)

def read_csv_from_storage():
    try:
        # Retrieve connection string from environment variable
        connection_string = os.environ["AzureWebJobsStorage"]
        
        # Initialize BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Define container name and blob name
        container_name = "mycontainer"
        blob_name = "example.csv"

        # Get the blob client
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        # Check if the blob exists
        if blob_client.exists():
            csv_data = blob_client.download_blob().content_as_text()
            df = pd.read_csv(io.StringIO(csv_data))
            return df.to_dict(orient='records')
        else:
            logging.warning(f"Blob '{blob_name}' read failed ")
            return f"Blob '{blob_name}' does not exist."

    except Exception as e:
        logging.error(f"Error reading blob: {e}")
        return str(e)
    

def read_blob_from_storage():
    try:
        # Retrieve connection string from environment variable
        connection_string = os.environ["AzureWebJobsStorage"]
        
        # Initialize BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Define container name and blob name
        container_name = "mycontainer"
        blob_name = "example.txt"

        # Get the blob client
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # Check if the blob exists
        if blob_client.exists():
            # Download the blob content
            download_stream = blob_client.download_blob()
            content = download_stream.readall()
            logging.info(f"Blob '{blob_name}' read successfully.")
            return content.decode("utf-8")  # Return as string
        else:
            logging.warning(f"Blob '{blob_name}' does not exist.")
            return f"Blob '{blob_name}' does not exist."

    except Exception as e:
        logging.error(f"Error reading blob: {e}")
        return str(e)
    

def list_blobs_in_container():
    try:
        # Retrieve connection string from environment variable
        connection_string = os.environ["AzureWebJobsStorage"]
        
        # Initialize BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Define container name
        container_name = "mycontainer"

        # Get the container client
        container_client = blob_service_client.get_container_client(container_name)

        # List all blobs in the container
        blob_list = container_client.list_blobs()
        blobs = [blob.name for blob in blob_list]
        logging.info(f"Blobs listed successfully: {blobs}")
        return blobs

    except Exception as e:
        logging.error(f"Error listing blobs: {e}")
        return str(e)

def delete_blob_from_storage(blob_name):
    try:
        # Retrieve connection string from environment variable
        connection_string = os.environ["AzureWebJobsStorage"]
        
        # Initialize BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Define container name
        container_name = "mycontainer"

        # Get the blob client
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        # Delete the blob
        if blob_client.exists():
            blob_client.delete_blob()
            logging.info(f"Blob '{blob_name}' deleted successfully.")
            return f"Blob '{blob_name}' deleted successfully."
        else:
            logging.warning(f"Blob '{blob_name}' does not exist.")
            return f"Blob '{blob_name}' does not exist."

    except Exception as e:
        logging.error(f"Error deleting blob: {e}")
        return str(e)