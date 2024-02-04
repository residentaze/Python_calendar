import json
import datetime
from dateutil import rrule
from User import User
import json


class Event:
    def __init__(self, title, organizer, description=None):
        self._title = title
        self._organizer = organizer
        self._description = description
        self._members = set()
        if isinstance(organizer, User):
            self._members.add(organizer)
        self._rate = []


    def __repr__(self):
        return f"Event('{self._title}', {self._members}, {self._description})"

    def get_title(self, title):
        return title

    def get_organizer(self):
        return self._organizer

    def get_frequency_event(self):
        return self._rate

    def create_event(self, start_date, rate, format="%Y,%m,%d"):
        start_date = datetime.datetime.strptime(start_date, format)
        end_date = start_date + datetime.timedelta(days=365 * 2)
        if rate == "once":
            self._rate.append(start_date)
        else:
            if rate == "ежедневный":
                rule = rrule.DAILY
            elif rate == "еженедельный":
                rule = rrule.WEEKLY
            elif rate == "ежемесячный":
                rule = rrule.MONTHLY
            elif rate == "ежегодный":
                rule = rrule.YEARLY
            else:
                print("Неверные данные.")
                return
            for date in rrule.rrule(rule, dtstart=start_date, until=end_date):
                self._rate.append(date)

    def add_part(self, admin, participant):
        if admin == self._organizer and isinstance(admin, User) and isinstance(participant, User):
            self._members.add(participant)
        else:
            raise ValueError("Некорректные участники события.")

    def get_members(self):
        return self._members

    def del_participants(self, admin, user):
        if admin == self._organizer and user in self._members:
            self._members.remove(user)
        else:
            raise ValueError("Некорректные участники события")

    def participants_leavе(self, user):
        if user in self._members and user != self._organizer:
            self._members.remove(user)

    def change_description(self, user, new_description):
        if user == self._organizer and isinstance(user, User):
            self._description = new_description
        else:
            raise ValueError("Вы не можете изменить описание")

    def del_description(self, user):
        if user == self._organizer and isinstance(user, User):
            self._description = None
        else:
            raise ValueError("Вы не можете удалить описание")

    def to_dict(self):
        event_dict = {
            'title': self._title,
            'organizer': self._organizer.to_dict(),
            'description': self._description,
            'participants': [participant.to_dict() for participant in self._members],
            'frequency': [dt.strftime("%Y-%m-%d") for dt in self._rate]
        }
        return event_dict

    def write_to_json(self, filename='event_data.json'):
        event_dict = self.to_dict()
        event_json = json.dumps(event_dict, indent=2)
        with open(filename, 'w') as file:
            file.write(event_json)

    @classmethod
    def from_dict(cls, event_dict):
        title = event_dict.get('title')
        organizer = User.from_dict(event_dict.get('organizer'))
        description = event_dict.get('description')
        participants = {User.from_dict(participant) for participant in event_dict.get('participants', [])}
        rate = [datetime.datetime.strptime(dt, "%Y-%m-%d").date() for dt in event_dict.get('frequency', [])]
        event = cls(title, organizer, description)
        event._members = participants
        event._rate = rate
        return event

    @classmethod
    def read_from_json(cls, file='event_data.json'):
        with open(file, 'r') as f:
            event_dict = json.loads(f.read())
        return cls.from_dict(event_dict)






