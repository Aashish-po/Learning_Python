import json
import warnings

import requests

warnings.filterwarnings("ignore")

url = "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json",
}
resp = requests.get(url, headers=headers, verify=True, timeout=10)
data = resp.json()
print("Full structure:")
print(json.dumps(data, indent=2)[:2000])
