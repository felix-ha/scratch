import requests
import json

url = 'http://127.0.0.1:5000/model'
data = {'prompt': 'Mach folgendes: Tue', 'info': 0.5}
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    response_data = response.json()
    prompt = response_data['prompt']
    info = response_data['info']

    print(response.text)
    print(f'prompt: {prompt}')
    print(f'Info: {info}')
else:
    print(f'Error: {response.status_code}')
