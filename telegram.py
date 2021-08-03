import requests
import json
import time
from datetime import date

today = date.today()
today=today.strftime("%d-%m-%Y")
header={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 "
                     "Safari/537.36"}

url = f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/11"

respons = requests.get(url=url, headers=header)
for i in respons.json()["districts"]:
    kk = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={i['district_id']}&date={today}"
    re = requests.get(url=kk)
    for j in re.json()["sessions"]:
        if j["available_capacity"]>0:
            if j["fee_type"]=="Free":
                    mass = "-----------------------------------------------------------\n\nVaccine Slot in Gujarat's  " \
                           "  (Free)   {}\ncenter_id : {}\nname : {}\naddress : {} - {} - {}\npincode : {" \
                           "}\n-----------------------------------------------------------\n\ndate -> {" \
                           "}\navailable_capacity -> {}\nmin_age_limit -> {}\ntime -> {" \
                           "}\n\n_________________________\nhttps://selfregistration.cowin.gov.in" \
                           "\n_________________________".format(
                        j["vaccine"], j["center_id"], j["name"], j["address"], j["block_name"], j["district_name"],
                        j["pincode"], today, j["available_capacity"], j["min_age_limit"], j["slots"])
                    bapu = requests.get(
                        "https://api.telegram.org/bot1880698050:AAEUJjZ_w8l80CArAwZOzCIKWWDvyVMSxkU/sendMessage"
                        "?chat_id=@help_for_vaccine_slots&text={}".format(mass))
                    print(bapu)

            else:
                mass = "-----------------------------------------------------------\n\nVaccine Slot in Gujarat's   (" \
                       "Paid-{})  {}\ncenter_id : {}\nname : {}\naddress: {} - {} - {} \npincode : {" \
                       "}\n-----------------------------------------------------------\n\ndate -> {" \
                       "}\navailable_capacity -> {}\nmin_age_limit -> {}\ntime -> {" \
                       "}\n\n_________________________\nhttps://selfregistration.cowin.gov.in" \
                       "\n_________________________".format(j["fee"],
                    j["vaccine"], j["center_id"], j["name"], j["address"], j["block_name"], j["district_name"],
                    j["pincode"], today, j["available_capacity"], j["min_age_limit"], j["slots"])
                bapu = requests.get(
                    "https://api.telegram.org/bot1880698050:AAEUJjZ_w8l80CArAwZOzCIKWWDvyVMSxkU/sendMessage?chat_id"
                    "=@help_for_vaccine_slots&text={}".format(
                        mass))
                print(bapu)
            break