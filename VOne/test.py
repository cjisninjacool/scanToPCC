import requests

url = "https://faxws-ha.us.retarus.com/rest/v1/12794us/fax/reports/FJL8C7ZLP418S6W5J2R0AW"


payload={}
headers = {
  'Authorization': 'Basic UHVyc3VlX0ZheEFQSTprdUA9MVJhay1OT1Q4dXNVYnJvZg=='
}

response = requests.request("GET", url, headers=headers)

print(response.text)
