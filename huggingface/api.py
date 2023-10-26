from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/model', methods=['POST'])
def model():
    data = request.get_json()
    prompt = data['prompt']
    info = data['info']
    response_data = {'prompt': prompt, 'info': info}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

