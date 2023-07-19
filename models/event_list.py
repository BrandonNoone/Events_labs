import datetime
from models.event import Event


event1 = Event("Mob programming", datetime.date(2023, 6, 19), 14, "The classroom", "we're gunna mob this lab")
event2 = Event("Glastonbury", datetime.date(2023, 6, 10), 10000,"glastonbury", "music, mugs")
events3 = Event("E3", datetime.date(2023, 9, 30), 8000,"LA", "gameepo")
events = [event1, event2, events3]

def add_new_event(event):
    events.append(event)
