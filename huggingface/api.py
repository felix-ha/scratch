from transformers import pipeline
import torch

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/model', methods=['POST'])
def model():
    data = request.get_json()
    prompt = data['prompt']
    prompt_format = "<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
    result = generator(prompt_format.format(prompt=prompt), do_sample=True, top_p=0.95, max_length=8192)
    info = data['info']
    response_data = {'result': result, 'info': info}
    return jsonify(response_data)

if __name__ == '__main__':
    generator = pipeline(model="LeoLM/leo-mistral-hessianai-7b-chat", device="cuda", torch_dtype=torch.float16)
    app.run(host="0.0.0.0", port=5000)
