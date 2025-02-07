
# Azure blob storage sample code
Some boilerplate code for your azure functions

## Azurite Storage Emulator
When using the Azurite storage emulator for local development and testing, you need to configure the AzureWebJobsStorage connection string to point to Azurite instead of an actual Azure Storage account in the cloud. Azurite provides a lightweight, local version of Azure Storage services (Blob, Queue, and Table) that you can use during development.

If you're working with Azure Functions in a local development environment, you can set the AzureWebJobsStorage value in the local.settings.json file. This file is used to store configuration settings for your function app during local development.

```
  {
    "IsEncrypted": false,
      "Values": {
        "AzureWebJobsStorage": "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;",
        "FUNCTIONS_WORKER_RUNTIME": "python"
      }
  }
```

Remember to start azurite blob service!
