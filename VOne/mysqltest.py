import pyodbc 
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
    print(payload)
    headers = {
        'Authorization': auth,
        'Content-Type': 'application/json'
    }   
    response = requests.request("POST", url, headers=headers, data=payload) 
    return response.text


server = 'Localhost' 
database = 'ScanTo' 
username = 'RetarusUploadUser' 
password = '!&w7d>@^-APnmt[+' 
cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Trusted_connection=yes;Server='+server+';Database='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()
#Sample select query
cursor.execute("exec get_Retarus_PendingOutbound") 
row = cursor.fetchone() 

def runn(cmd):
    cursor.execute(cmd)
list_one = []
list_two  = []
try:
    #print(x)
    while row:
        number = row[0]
        email = row[1]
        reference = row[2]
        FaxImageFormat = row[3]
        alerttype = row[4]
        RecordId = row[5]
        RetarusAuth = row[6]
        global responce
        print(alerttype)
        responce = run(number=number,rerefrence=reference,sucessEmail=email,failureEmail=email,attachedFaxImageMode=alerttype,attachedFaxImageFormat=FaxImageFormat, auth=RetarusAuth)
        list_one.append(responce)
        print(responce)
        list_two.append(str(RecordId))
        row = cursor.fetchone()

    for i in list_one:
        #runn(list_one,list_two)
        #"exec upd_eFaxJobID '"+str(list_one)+"', "+str(list_two)
        list_one = list_one[0]
        list_one = json.loads(list_one)
        list_one = (list_one["jobId"])
        list_two = int(list_two[0])
        runn("exec upd_eFaxJobID '"+str(list_one)+"', '"+str(list_two)+"'")
        cnxn.commit()   #Run function!!!

except Exception as e:
    e = str(e)
    e = e.replace("'","")
    print("[dbo].[ins_RetarusErrors]'" + str(e)+"'")
    runn("[dbo].[ins_RetarusErrors] '" + str(e)+"'")
    cnxn.commit() 
    pass







