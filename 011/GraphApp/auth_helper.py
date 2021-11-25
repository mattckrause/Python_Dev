import yaml
import logging
from msal import ConfidentialClientApplication


with open(r"C:\Dev\Python_Dev\011\GraphApp\auth_config.yml", "r") as yamlfile:
    config = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")


# Create a preferably long-lived app instance which maintains a token cache.
app = ConfidentialClientApplication(
    config["client_id"], authority=config["authority"],
    client_credential=config["secret"],
    # token_cache=...  # Default cache is in memory only.
    # You can learn how to use SerializableTokenCache from
    # https://msal-python.rtfd.io/en/latest/#msal.SerializableTokenCache
    )

# The pattern to acquire a token looks like this.
result = None

# Firstly, looks up a token from cache
# Since we are looking for token for the current app, NOT for an end user,
# notice we give account parameter as None.
result = app.acquire_token_silent(config["scope"], account=None)

if not result:
    logging.info(
        "No suitable token exists in cache. Let's get a new one from AAD.")
    result = app.acquire_token_for_client(scopes=config["scope"])

if "access_token" in result:
    print(result.get("access_token"))
else:
    print(result.get("error"))
    print(result.get("error_description"))
    # You may need this when reporting a bug
    print(result.get("correlation_id"))
