import pyodbc 
import requests
import json
server = 'P00196C' 
database = 'ScanTo' 
username = 'RetarusUploadUser' 
password = '!&w7d>@^-APnmt[+' 
cnxn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Trusted_connection=yes;Server='+server+';Database='+database+';UID='+username+';PWD='+password)
cursor = cnxn.cursor()
cursor.execute("exec get_Retarus_MissingStatus") 
row = cursor.fetchone() 
#Test
jobStatList = []
list_two = []
status_list = []
reason_list = []
sentTsList = []
sentToNumberList=[]
remoteCsidList = []
pagesList = []
while row:
    #print(row[0],row[1])

    url = "https://faxws-ha.us.retarus.com/rest/v1/12794us/fax/reports/"+row[0]
   # print(url)
    payload={}
    headers = {
    'Authorization': row[1]
    }

    response = requests.request("GET", url, headers=headers)
    print(response.json())
    de = (response.json())
    jobStatus = response.json()
    try:
        jobStatList.append(row[0])
    except:
        pass
    status = (de['recipientStatus'][0]["status"])
    reason = (de['recipientStatus'][0]["reason"])
    sentTs = (de['recipientStatus'][0]["sentTs"])
    sentToNumber = (de['recipientStatus'][0]["sentToNumber"])
    remoteCsid = (de['recipientStatus'][0]["remoteCsid"])
    pages = de['pages']
    status_list.append(status)
    reason_list.append(reason)
    sentTsList.append(sentTs)
    sentToNumberList.append(sentToNumber)
    remoteCsidList.append(remoteCsid)
    pagesList.append(pages)


    list_two.append(jobStatus)

    row = cursor.fetchone()

print(status_list,reason_list,sentTsList,sentToNumberList,remoteCsidList,pagesList)
for i in range(len(jobStatList)):
    print(i)
    print(row)
    #print("exec upd_Retarus_Status '"+ str(status_list[i])+ "','"+ str(reason_list[i])+ "','"+ str(sentTsList[i])+ "','"+ str(sentToNumberList[i])+ "','"+ str(remoteCsidList[i])+ "','"+ str(pagesList[i])+ "','" + str(jobStatList[i])+"'")
    cursor.execute("exec upd_Retarus_Status '"+ str(status_list[i])+ "','"+ str(reason_list[i])+ "','"+ str(sentTsList[i])+ "','"+ str(sentToNumberList[i])+ "','"+ str(remoteCsidList[i])+ "','"+ str(pagesList[i])+ "','" + str(jobStatList[i])+"'") 
    cursor.commit()   
