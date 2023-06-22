import logging
import io
import base64
import tempfile
import azure.functions as func
from os import listdir
from azure.storage.filedatalake import DataLakeFileClient

#variables
connectionString = "DefaultEndpointsProtocol=https;AccountName=mksynapsestorage;AccountKey=U4Hwt57KClMClLZVREVoC0IelCh9I7P0PgzmyGO98Ijwcx4quQnCWoSVFUJGETFuV6Ijuf7ZIw+/+AStd32XZQ==;EndpointSuffix=core.windows.net"
#fileSystem = "attachments/messages"
#sourceLocation = "cdda6ada-cace-4b53-bf70-6f63fe5f049d_0_0"

app = func.FunctionApp()
# Learn more at aka.ms/pythonprogrammingmodel
# Get started by running the following code to create a function using a HTTP trigger.
@app.function_name(name="AttachmentDownload")
@app.route(route="hello")

def main(req):
    #get temp file 
    tempFilePath = tempfile.gettempdir()
    fp = tempfile.NamedTemporaryFile()

    file = DataLakeFileClient.from_connection_string("DefaultEndpointsProtocol=https;AccountName=mksynapsestorage;AccountKey=U4Hwt57KClMClLZVREVoC0IelCh9I7P0PgzmyGO98Ijwcx4quQnCWoSVFUJGETFuV6Ijuf7ZIw+/+AStd32XZQ==;EndpointSuffix=core.windows.net",
                                                            file_system_name="attachments", file_path="messages")
    #file_system_client = service_client.get_file_system_client(file_system="attachments")
    #directory_client = file_system_client.get_directory_client("messages")
    #file_client = directory_client.get_file_client("cdda6ada-cace-4b53-bf70-6f63fe5f049d_0_0")
    #download=file_client.download_file()
    #downloaded_bytes = download.readall()
    #with open("C:/Temp/test.json", "wb") as my_file:
    #    download = file.download_file()#my_file.write(downloaded_bytes)
    #    download.readinto(my_file)
    #    my_file.close()
    return file
    #return f'Hello'


'''
def test_function(req: func.HttpRequest) -> func.HttpResponse:
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
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
'''