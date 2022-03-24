import requests

token =  ''

response = requests.put("https://integration.visma.net/API/controller/api/v1/customer/1212",
    json={
        "mainAddress": {
            "value": {
                "addressLine1": {
                    "value": "Karenslyst Alle 56"
                },                              
                "postalCode": {
                    "value": "0277"
                },
                "city": {
                    "value": "Oslo"
                }
            }
        }
    },
    headers={
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token,
        'ipp-company-id': '1113659',
        'ipp-application-type': 'Visma.net Financials'
    }
)

if response.status_code == 204:
    print("OK")
