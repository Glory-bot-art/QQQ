import requests
from datetime import datetime,timedelta

#getting data with request and using j sonnnnn
url ="https://nfs.faireconomy.media/ff_calendar_thisweek.json"
response = requests.get(url)
events: list[dict] = response.json()

#writing logic for date
today = datetime.today().date()
tommrow = today+timedelta(days=1)

#it time to loop through it 