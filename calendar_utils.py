# calendar_utils.py - Google Calendar integration logic
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Add full calendar IDs here — these can be from different Google accounts
CALENDAR_IDS = [
    'courtney.watson@cfa.harvard.edu'
]

CALENDAR_COLORS = {
    'courtney.watson@cfa.harvard.edu': "#B640FA",
}

def get_combined_calendar_events():
    creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
    service = build("calendar", "v3", credentials=creds)

    now = datetime.utcnow().isoformat() + "Z"
    end = (datetime.utcnow() + timedelta(days=90)).isoformat() + "Z"
    events_list = []

    for calendar_id in CALENDAR_IDS:
        events_result = service.events().list(
            calendarId=calendar_id,
            timeMin=now,
            timeMax=end,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])
        for event in events:
            start_time = event["start"].get("dateTime", event["start"].get("date"))
            events_list.append({
                "title": event.get("summary", "No Title"),
                "start": start_time,
                "color": CALENDAR_COLORS.get(calendar_id, "#FFFFFF"),
            })

    return sorted(events_list, key=lambda x: x["start"])
