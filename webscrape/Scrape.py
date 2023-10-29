import requests
from bs4 import BeautifulSoup
from azure.communication.email import EmailClient

def scrape_table(url):
	# Send a GET request to the website URL
	response = requests.get(url)

	# Parse the HTML content of the website
	soup = BeautifulSoup(response.content, 'html.parser')

	# Find the specific table
	table = soup.find('div', class_='table-responsive')
	content = table.find_all('a')

	# Extract the contents of the table
	#table_contents = table.text

	# Return the contents of the table
	return content

def send_results(payload):
	try:
		connection_string = 'connection_string'
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

	except Exception as ex:
		print(ex)

search = "Grothdarr"
r = scrape_table("https://eso-hub.com/en/golden-vendor")
for element in r:
	if search in element.text:
		print("{} is on sale!".format(search))
		#send_results("{} is on sale!".format(search))
		break
