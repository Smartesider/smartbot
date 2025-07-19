from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import pytz

class CalendarService:
    def __init__(self, credentials_file):
        self.credentials = service_account.Credentials.from_service_account_file(credentials_file)
        self.service = build('calendar', 'v3', credentials=self.credentials)

    def create_event(self, calendar_id, event_details):
        event = {
            'summary': event_details['summary'],
            'location': event_details.get('location', ''),
            'description': event_details.get('description', ''),
            'start': {
                'dateTime': event_details['start'].isoformat(),
                'timeZone': event_details.get('timeZone', 'UTC'),
            },
            'end': {
                'dateTime': event_details['end'].isoformat(),
                'timeZone': event_details.get('timeZone', 'UTC'),
            },
            'attendees': [{'email': attendee} for attendee in event_details.get('attendees', [])],
        }
        event = self.service.events().insert(calendarId=calendar_id, body=event).execute()
        return event

    def move_event(self, calendar_id, event_id, new_start, new_end):
        event = self.service.events().get(calendarId=calendar_id, eventId=event_id).execute()
        event['start']['dateTime'] = new_start.isoformat()
        event['end']['dateTime'] = new_end.isoformat()
        updated_event = self.service.events().update(calendarId=calendar_id, eventId=event_id, body=event).execute()
        return updated_event

    def cancel_event(self, calendar_id, event_id):
        self.service.events().delete(calendarId=calendar_id, eventId=event_id).execute()

    def check_availability(self, calendar_id, time_min, time_max):
        body = {
            "timeMin": time_min.isoformat(),
            "timeMax": time_max.isoformat(),
            "items": [{"id": calendar_id}]
        }
        freebusy_query = self.service.freebusy().query(body=body).execute()
        return freebusy_query['calendars'][calendar_id]['busy']