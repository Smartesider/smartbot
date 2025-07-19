from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pytz

# Initialize Google Calendar API
def initialize_calendar_api(credentials_file):
    credentials = service_account.Credentials.from_service_account_file(credentials_file)
    service = build('calendar', 'v3', credentials=credentials)
    return service

# Check free/busy times for a given time range
def check_free_busy(service, calendar_id, start_time, end_time):
    body = {
        "timeMin": start_time.isoformat(),
        "timeMax": end_time.isoformat(),
        "items": [{"id": calendar_id}]
    }
    freebusy_query = service.freebusy().query(body=body).execute()
    return freebusy_query

# Create an event in Google Calendar
def create_event(service, calendar_id, event_details):
    event = {
        'summary': event_details['summary'],
        'location': event_details.get('location', ''),
        'description': event_details.get('description', ''),
        'start': {
            'dateTime': event_details['start_time'].isoformat(),
            'timeZone': event_details.get('time_zone', 'UTC'),
        },
        'end': {
            'dateTime': event_details['end_time'].isoformat(),
            'timeZone': event_details.get('time_zone', 'UTC'),
        },
        'attendees': event_details.get('attendees', []),
    }
    created_event = service.events().insert(calendarId=calendar_id, body=event).execute()
    return created_event

# Move an event in Google Calendar
def move_event(service, calendar_id, event_id, new_start_time, new_end_time):
    event = service.events().get(calendarId=calendar_id, eventId=event_id).execute()
    event['start']['dateTime'] = new_start_time.isoformat()
    event['end']['dateTime'] = new_end_time.isoformat()
    updated_event = service.events().update(calendarId=calendar_id, eventId=event_id, body=event).execute()
    return updated_event

# Cancel an event in Google Calendar
def cancel_event(service, calendar_id, event_id):
    service.events().delete(calendarId=calendar_id, eventId=event_id).execute()
    return {"status": "Event deleted successfully."}