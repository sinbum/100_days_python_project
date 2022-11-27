import requests
import datetime
from package.time_convert import TimeConvert

sunrise = TimeConvert()
sunset = TimeConvert()

MY_LAT = 37.616850
MY_LONG = 127.044799

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()["results"]

# Todo 1. GMT+9 계산 필요. (완료)
sunrise.set_all_time(data["sunrise"])
sunset.set_all_time(data["sunset"])

time_now = datetime.datetime.now()

while True:
    if time_now.hour >= sunset.get_datetime_class().hour \
            or time_now.hour <= sunrise.get_datetime_class().hour:
        print("now is night")
    else :
        print("now is morning or afternoon")

# Todo 2. messge 보내기