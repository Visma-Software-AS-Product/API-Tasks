import requests
import json
 
token =  ''
 
response = requests.get("https://integration.visma.net/API/security/api/v1/token/usercontexts",
                      headers={'Accept': 'application/json',
                               'Authorization': 'Bearer ' + token}
                    )
 
if response.status_code == 200:
 data = json.loads(response.text)
 for context in data:
  print(context["id"])
  print(context["name"])
