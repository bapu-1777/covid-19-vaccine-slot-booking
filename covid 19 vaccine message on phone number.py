import requests
import pyrebase
import random
from datetime import date
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
today = date.today()
today=today.strftime("%d-%m-%Y")
headers={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
def ma(mass,x):
    import pywhatkit
    pywhatkit.sendwhatmsg("+91 "+x,mass, 10, 49)
def phone(mass,x):
    from twilio.rest import Client
    client = Client("ACf6399e1dfcb0ab278597acd264f82292", "3898e155b86aa06be9615352b5b30513")
    client.messages.create(to=["+91 "+x],
                           from_="+12014643899",
                           body=mass)
def aphone(mass,x):
    import requests
    resp = requests.post('https://textbelt.com/text', {
        'phone': "+91 "+x,
        'message': mass,
        'key': 'textbelt',
    })
    print(resp.json())
data=db.child("pincode").get()
for data1 in data.each():
    x=data1.val()["phone"]
    y=data1.val()["pincode"]
    url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=110001&date=09-06-2021"
    responsx = requests.get(url=url, headers=headers)
    print(responsx)
    datax = responsx.json()
    if len(datax["sessions"]) > 0:
        for j in datax["sessions"]:
            if j["available_capacity"]>0:
                mass = "-----------------------------------------------------------\n\nVaccine Slot in Gujarat's   (" \
                       "Paid-{})  {}\ncenter_id : {}\nname : {}\naddress: {} - {} - {} \npincode : {" \
                       "}\n-----------------------------------------------------------\n\ndate -> {" \
                       "}\navailable_capacity -> {}\nmin_age_limit -> {}\ntime -> {" \
                       "}\n\n_________________________\nhttps://selfregistration.cowin.gov.in" \
                       "\n_________________________".format(j["fee"],
                                                            j["vaccine"], j["center_id"], j["name"], j["address"],
                                                            j["block_name"], j["district_name"],
                                                            j["pincode"], today, j["available_capacity"],
                                                            j["min_age_limit"], j["slots"])
                print("ll")
                # ma(mass,x)
                phone(mass,x)
                # aphone(mass,x)


