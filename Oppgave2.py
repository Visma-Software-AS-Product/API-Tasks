import requests
import json
 
token =  ''
 
response = requests.get(
	'https://integration.visma.net/API/controller/api/v1/customer',
	params={
		'pageNumber': 1,
		'pageSize': 20,                            
    },
	headers={
		'Accept': 'application/json',
		'Authorization': 'Bearer ' + token,
		'ipp-company-id': '1113659',
		'ipp-application-type': 'Visma.net Financials'
    }
)
 
if response.status_code == 200:
	customers = json.loads(response.text)
	
	for customer in customers:
		print(str(customer["number"]) + " - " + customer["name"])