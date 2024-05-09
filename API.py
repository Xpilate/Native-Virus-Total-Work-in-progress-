import base64
import requests
import json
from virusui import query 


#Malicious URLS DATA BASE - https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset
#Storage of Converted Links to Base64 representation
convertId = []
jsResponse = []
responseList = []
#API Key    
api_key = '35db2d2571a38eac18a3db4951d283338c126a754225db46ddb5c6072512b100'
def urlReport(url_id):
 #         Adds the converted LINK to the end of request
 url = "https://www.virustotal.com/api/v3/urls/" + url_id

 headers = {
    "accept": "application/json",
    "x-apikey": api_key
}
 response = requests.get(url, headers=headers)
 return response.json()
def is_harmless(response):
 #parses through onject
 return response.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("harmless")
def is_malicious(response):
 #parses through object
 return response.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("malicious")
#Grabs Data from VirusUI (Front End) 
#Then Converts and adds the new information to a new array
for url in query: 
  url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
  print(url_id)
  convertId.append(url_id)
#For each index in CovertId List
for x in convertId:
  jsonx = urlReport(x)   
  jsResponse.append(jsonx)
for response in jsResponse: 
 harmless = is_harmless(response)
 malicious = is_malicious(response)
 print(f"HARMLESS: {harmless}")
 print(f"MALICIOUS: {malicious}") 
for x in query:
  responseList.append(f"HARMLESS: {harmless} and MALICIOUS: {malicious}")
print(responseList)



 
 

 
 



 
   
 
  
 
  
  
 




  
 
 





