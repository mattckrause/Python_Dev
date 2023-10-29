import azure.functions as func
import logging
import requests
from bs4 import BeautifulSoup
from azure.communication.email import EmailClient

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
@app.route(route="httplearning")
def httplearning(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    search = "Grothdarr"
    r = scrape_table("https://eso-hub.com/en/golden-vendor")
    for line in r:
        if search in line.text:
            send_results("{} is on sale!".format(search))
            break
        else:
            return func.HttpResponse(f"Item not found", status_code=200)

def scrape_table(url):
    # Send a GET request to the website URL
    response = requests.get(url)
    # Parse the HTML content of the website
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the specific table
    table = soup.find('div', class_='table-responsive')
    content = table.find_all('a')
    return content

def send_results(payload):
    try:
        connection_string = ''
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": "DoNotReply@b347bfa6-f5e7-40df-8523-b59be6bcadee.azurecomm.net",
            "recipients":  {
                "to": [{"address": "7193428991@vtext.com" }],
            },
            "content": {
                "subject": "ESO Golden Vendor Update",
                "plainText": payload,
            }
        }
        poller = client.begin_send(message)
        result = poller.result()
        return func.HttpResponse(f"Sending message: {message}", status_code=200)

    except Exception as ex:
        return func.HttpResponse(f"Exception: {ex}", status_code=500)
