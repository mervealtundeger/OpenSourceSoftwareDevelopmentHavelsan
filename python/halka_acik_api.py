import requests
response = requests.get("https://api.ebird.org/v2/ref/taxonomy/versions")
print("\n",response.json())
#HalkaAcikApiyeSorguAtma