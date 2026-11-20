import requests
from datetime import datetime,timedelta


def calendar()->dict[str,list[dict]]:
    url = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    response.raise_for_status()
    events = response.json()

    today = datetime.now().astimezone().date()
    tomorrow = today + timedelta(days=1)

    today_high = []
    tomorrow_high =[]


    for event in events:
        if event.get("impact")!="High":
            continue
        

    event_dt = datetime.fromisoformat(event["date"]).astimezone()
    event_date = event_dt.date()

    if event_date == today:
        today_high.append(event)
    elif event_date ==tomorrow:
        tomorrow_high.append(event)


    return{
        "today":today_high,
        "tomorrow":tomorrow_high

    }
print(calendar())