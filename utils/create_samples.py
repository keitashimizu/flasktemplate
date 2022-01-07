import json
from faker import Faker
import urllib.request

fake = Faker("ja_JP")

url = "http://localhost:5000/api/users"

for i in range(500):
    data = {
        "name":fake.name(),
        "address":fake.address(),
        "tel":fake.phone_number(),
        "mail":fake.ascii_email()
    }
    headers = {
        'Content-Type': 'application/json'
    }

    req = urllib.request.Request(url, json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body)