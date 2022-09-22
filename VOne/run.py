import requests
import json

def run(number = "6614344192",name = "207d0199-6165-4839-b424-26bbdaf0ba74.pdf",rerefrence="https://ipursue.tech/scantodocs/1-1/207d0199-6165-4839-b424-26bbdaf0ba74.pdf",sucessEmail = "colin.hart@pursuehealthllc.com",failureEmail = "colin.hart@pursuehealthllc.com",attachedFaxImageMode = "SUCCESS_ONLY",attachedFaxImageFormat = "PDF",auth = 'Basic UHVyc3VlX0ZheEFQSTprdUA9MVJhay1OT1Q4dXNVYnJvZg=='):
  url = "https://faxws-ha.us.retarus.com/rest/v1/12794US/fax"

  payload = json.dumps({
    "recipients": [
      {
        "number": number
      }
    ],
    "documents": [
      {
        "name": name,
        "reference": rerefrence,
        "data": None
      }
    ],
    "statusReportOptions": {
      "reportMail": {
        "successAddress": sucessEmail,
        "failureAddress": failureEmail,
        "attachedFaxImageMode": attachedFaxImageMode,
        "attachedFaxImageFormat": attachedFaxImageFormat
      }
    }
  })
  headers = {
    'Authorization': auth,
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)

