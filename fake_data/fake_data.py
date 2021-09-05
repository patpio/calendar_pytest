import datetime
import json
import os
import random


class EventGenerator:
    def __init__(self):
        self.titles = ['Learn python', 'Practise python', 'Do python exam', 'Pass python exam']
        self.people = ['Ola', 'Ela', 'Ala']
        self.labels = ['Private', 'Business']

    def generate(self, amount):
        with open(os.path.join('.', 'data.json'), 'w') as file:
            data = {
                'meetings': [],
                'workshops': []
            }

            for no in range(1, amount + 1):
                item = {
                    'title': random.choice(self.titles),
                    'start_time': str(
                        datetime.datetime.now() + datetime.timedelta(minutes=float(random.randint(1000, 10000)))),
                    'duration': random.randint(15, 1000),
                    'owner': random.choice(self.people),
                    'participants': [random.choice(self.people) for _ in range(1, random.randint(1, 5))],
                    'labels': random.choice(self.labels)
                }
                data['meetings'].append(item)

            json.dump(data, file)


d = EventGenerator()
d.generate(50)
