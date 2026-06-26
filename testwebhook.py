import requests

data = {
    "name": "Ayo",
    "email": "ayo@example.com",
    "company": "Eternal",
    "message": "Hello world"
}

response = requests.post(
    "http://127.0.0.1:5000/webhook", json=data
)

print(response.json())