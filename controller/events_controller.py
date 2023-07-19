from flask import Blueprint, render_template, request
from models.event import Event
from models.event_list import events, add_new_event


events_blueprint = Blueprint("events",__name__)
#INDEX, display all events
@events_blueprint.route("/events")
def index():
    return render_template("index.jinja", title="Events Page", event_list=events) 

@events_blueprint.route("/events", methods = ["POST"])
def add_events():
    event_name = request.form["events"]
    event_date = request.form["date"]
    event_number_of_guests = request.form["guest"]
    event_location = request.form ["location"]
    event_description = request.form["description"]
    new_event = Event(event_name, event_date, event_number_of_guests ,event_location ,event_description)
    add_new_event(new_event)
    return render_template("index.jinja", title="My event list", event_list=events)