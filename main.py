import requests
import datetime,timedelta


def calender()->dict[str,list[dict]]:
    url = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"

# Adding a User-Agent helps prevent 403/429 blocks from Cloudflare
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
