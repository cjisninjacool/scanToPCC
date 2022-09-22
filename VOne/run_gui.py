import tkinter
root = tkinter.Tk()

import requests
import json

url = "https://faxws-ha.us.retarus.com/rest/v1/12794US/fax"

payload = json.dumps({
  "recipients": [
    {
      "number": "6614344192"
    }
  ],
  "documents": [
    {
      "name": "207d0199-6165-4839-b424-26bbdaf0ba74.pdf",
      "reference": "https://ipursue.tech/scantodocs/1-1/207d0199-6165-4839-b424-26bbdaf0ba74.pdf",
      "data": None
    }
  ],
  "statusReportOptions": {
    "reportMail": {
      "successAddress": "colin.hart@pursuehealthllc.com",
      "failureAddress": "colin.hart@pursuehealthllc.com",
      "attachedFaxImageMode": "SUCCESS_ONLY",
      "attachedFaxImageFormat": "PDF"
    }
  }
})
headers = {
  'Authorization': 'Basic UHVyc3VlX0ZheEFQSTprdUA9MVJhay1OT1Q4dXNVYnJvZg==',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

labe = tkinter.Label(text="Sucess").pack()
label = tkinter.Label(text=response.text).pack()
root.mainloop()