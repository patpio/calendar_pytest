import datetime

import pytest

from src.event import Event


@pytest.fixture
def event_data():
    event = {
        'title': 'Learn Python',
        'start_time': datetime.datetime(2021, 9, 6, 10, 30),
        'duration': datetime.timedelta(hours=1),
        'owner': 'Pat',
        'participants': ['John']
    }
    yield event


@pytest.fixture
def monkeypatch_datetime_now(event_data, monkeypatch, request):
    marker = request.node.get_closest_marker('duration')
    if marker is None:
        duration = 60
    else:
        duration = marker.args[0]

    fake_now = event_data['start_time'] - datetime.timedelta(minutes=duration)

    class MyDatetime:
        @classmethod
        def now(cls):
            return fake_now

    monkeypatch.setattr(datetime, 'datetime', MyDatetime)


def test_create_event_instance(event_data, monkeypatch_datetime_now):
    event = Event(**event_data)

    assert repr(event) == 'Event(title="Learn Python", start_time=datetime.datetime(2021, 9, 6, 10, 30), ' \
                          'duration=datetime.timedelta(seconds=3600), owner="Pat", participants=[\'John\'])'


def test_event_duration_one_hour(event_data):
    event = Event(**event_data)

    assert event.duration.seconds == 60 * 60


def test_event_duration_ten_minutes(event_data):

    event_data['duration'] = datetime.timedelta(minutes=10)

    with pytest.raises(ValueError) as excinfo:
        Event(**event_data)

    assert 'duration' in str(excinfo.value)


def test_event_duration_change_to_ten_minutes(event_data):
    event = Event(**event_data)

    with pytest.raises(ValueError) as excinfo:
        event.duration = datetime.timedelta(minutes=10)

    assert 'duration' in str(excinfo.value)


def test_start_time_begins_in_one_hour(event_data, monkeypatch_datetime_now):
    Event(**event_data)


@pytest.mark.duration(5)
def test_start_time_begins_in_five_minutes(event_data, monkeypatch_datetime_now):

    with pytest.raises(ValueError) as excinfo:
        Event(**event_data)

    assert 'start_time' in str(excinfo.value)
