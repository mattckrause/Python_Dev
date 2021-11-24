import json
import msal
import os


# Load the oauth_settings.yml file
settings = json.load(open('C:/dev/Python_Dev/011/GraphApp/auth_config.json', 'r'))



# print(stream)
# settings = json.load(stream)

print(settings)