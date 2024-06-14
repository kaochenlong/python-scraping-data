import os
import requests
from datetime import datetime
from dotenv import load_dotenv
from urllib.parse import urlencode

load_dotenv()

API_KEY = os.getenv("CWA_API_KEY")

if API_KEY is None:
    raise ValueError("請先設定 API_KEY")

END_POINT = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001"

params = {
    "Authorization": API_KEY,
    "format": "JSON",
    "AreaName": "花蓮縣",
}

URL = f"{END_POINT}?{urlencode(params)}"

response = requests.get(URL, headers={"accept": "application/json"})
data = response.json()

output = f"{"日期":15}地震規模\n"

for record in reversed(data["records"]["Earthquake"]):
    info = record["EarthquakeInfo"]
    date = datetime.strptime(info["OriginTime"], "%Y-%m-%d %H:%M:%S")
    date_str = date.strftime("%Y/%m/%d")
    value = info["EarthquakeMagnitude"]["MagnitudeValue"]
    output += f"{date_str:15} {value}\n"

print(output)
