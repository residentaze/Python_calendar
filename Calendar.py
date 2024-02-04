
from User import User
from Event import Event
import datetime


class Calendar:

    def __init__(self):
        self._calendar = {}


    def __str__(self):
        return f"{self._calendar}"

    def add_event(self, event):
        if not isinstance(event, Event):
            raise ValueError("error.")
        event_dat = event.get_frequency_event()
        for date in event_dat:
            if date in self._calendar:
                self._calendar[date].append(event)
            else:
                self._calendar[date] = [event]

    def rm_event(self, i):
        if i in self._calendar:
            self._calendar.pop(i, None)

    def search_event(self, start_date, end_date):
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
        events_in_range = []
        for date, events in self._calendar.items():
            if start_date <= date.date() <= end_date:
                events_in_range.extend(events)
        return events_in_range

    def del_event(self, user):
        if user == self._organizer and isinstance(user, User):
            self._calendar.remove_event(self)
        else:
            raise ValueError("Только организатор может удалить событие")
