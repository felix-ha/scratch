import requests
import json

context = ""
question = ""
qa_prompt = f"Gegeben diesem Kontext: {context} \n Beantworte die Frage: {question}"

url = 'http://:5000/model'
data = {'prompt': qa_prompt, 'info': 0.5}
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    response_data = response.json()
    result = response_data['result']
    info = response_data['info']
    print(result[0]['generated_text'])


else:
    print(f'Error: {response.status_code}')
