import random
import time
from datetime import datetime

import requests
from django.apps import AppConfig
def execute_this():
    first_names=('a','e','i','o','u')
    last_names=('b','c','d','f','g','h')
    start =0
    while time.clock()-start<10:
        group = "".join(random.choice(first_names)+""+random.choice(last_names) for _ in range(7))
        group += str(datetime.now())
        requests.post('https://messaging-app-d8013.firebaseio.com/messages.json', json={"message": group})
        print(group)
        time.sleep(1)

class FirebaseConfig(AppConfig):
    name = 'firebase'

    def ready(self):
        execute_this()
