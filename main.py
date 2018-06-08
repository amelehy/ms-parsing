#!/usr/bin/env python

import json
from pprint import pprint
import requests
import glob, os

AUTH_HEADER = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImlCakwxUmNxemhpeTRmcHhJeGRacW9oTTJZayIsImtpZCI6ImlCakwxUmNxemhpeTRmcHhJeGRacW9oTTJZayJ9.eyJhdWQiOiJodHRwczovL2FwaS5wYXJ0bmVyY2VudGVyLm1pY3Jvc29mdC5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC83MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDcvIiwiaWF0IjoxNTI4MzQ4NDg0LCJuYmYiOjE1MjgzNDg0ODQsImV4cCI6MTUyODM1MjM4NCwiYWlvIjoiWTJkZ1lNampPRHhIdlhPZW9VbmNmWW5WQnphN0F3QT0iLCJhcHBpZCI6IjRkMDE0NGI2LTBlZGUtNGY1Ni05ZTgwLTdhMjg0M2RmMGQxZCIsImFwcGlkYWNyIjoiMSIsImVfZXhwIjoyNjI4MDAsImlkcCI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzcyZjk4OGJmLTg2ZjEtNDFhZi05MWFiLTJkN2NkMDExZGI0Ny8iLCJvaWQiOiI2OGFjMTVhZC0wZmNkLTRlYWYtYmY0Ny1kODZlYzAyNWIxYjUiLCJzdWIiOiI2OGFjMTVhZC0wZmNkLTRlYWYtYmY0Ny1kODZlYzAyNWIxYjUiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiV1ciLCJ0aWQiOiI3MmY5ODhiZi04NmYxLTQxYWYtOTFhYi0yZDdjZDAxMWRiNDciLCJ1dGkiOiJmdnFHMVNsT0UwS0xfQktzVndnMUFBIiwidmVyIjoiMS4wIn0.QegvgI6ILcRal-nkvqlH4OM07plX8xmFYSRcBKZaXyXZ4ckUzrsOLduTRj1oguLuV2hqYnFOV-Hu9Zg9A9Nx_JlR7jsk0MXaQgEDhTJHpiQSqrjlHnq-zAjcvaCtacbEQXA4mT8uTECygN3OYtIENQ7IqlVCUo1LNaY_sw36TWnPcAJgrs46gPjJyCIp65gutHV9b1mreNZEvZfsil6hfBeokN8_S5SU77ZDnvQqUARbZevzcRHOdToA1CHled4vhUivQnT1eP7GMX67U3s8r03R1z4u4DmRbSUt1kj7xQXsn0UaBcdIPKe7vfmICbTGqJImT0pHkVxTEZ3aj9dw-Q"

os.chdir("./")
for file in glob.glob("*.json"):
    with open(file) as f:
        data = json.load(f)

        items = data['matchingPartners']['items']

        for item in items:
            baseUrl = 'https://api.partnercenter.microsoft.com/partnerfinder/v1/marketingprofiles/'
            newUrl = baseUrl + item['partnerId']

            headers = {'ocp-apim-subscription-key': 'c306f5dd740f4946920822865932a356', 'Authorization': AUTH_HEADER}
            request = requests.get(newUrl, headers=headers)
            payload = json.loads(request.text)
            print payload[0]['name'] + ', ' + payload[0]['url']

