import requests


url = 'http://127.0.0.1:8050/api'

data = {
        'text1': 'Apple Inc.',
        'text2': 'Apple Incorporated'
        }

response = requests.get(url, params=data)

if response.status_code == 200:
    print(response.text)
else:
    print("Request failed:", response.status_code)