import requests
import pyrebase
import random


firebaseConfiger={
    "apiKey": "AIzaSyB1QvcbgGGcbs23QyfH_xChydmK4XBOSVQ",
    "authDomain": "covid-all-94dca.firebaseapp.com",
    "databaseURL": "https://covid-all-94dca-default-rtdb.firebaseio.com",
    "projectId": "covid-all-94dca",
    "storageBucket": "covid-all-94dca.appspot.com",
    "messagingSenderId": "46777012183",
    "appId": "1:46777012183:web:331b39c00d9474f92bc592",
    "measurementId": "G-HMNM6EWGQP"
}
firebase=pyrebase.initialize_app(firebaseConfiger)
db=firebase.database()





url="https://cdn-api.co-vin.in/api/v2/admin/location/districts/11"
headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

respons=requests.get(url=url,headers=headers)
data=respons.json()

for i in data["districts"]:
   kk=str(i["district_id"])
   url1 = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={kk}&date=08-06-2021"
   responsx = requests.get(url=url1, headers=headers)
   print(responsx)
   datax = responsx.json()
   th={}
   if len(datax["sessions"])>0:
       for j in datax["sessions"]:
           th["name"]=j["name"]
           th["state"]=j["state_name"]
           th["dis"]=j["district_name"]
           th["area"]=j["block_name"]
           th["phone"]="7878374787"
           th["pincode"]=j["pincode"]
           th["available"]=str(random.randrange(0, 33))
           th["time"]=random.choice(j["slots"])
           th["type"]=random.choice(["free","free","paid - 150","paid - 100"])
           db.child("tifin").child("s2").set(th)
           th.clear()
           break
   break
