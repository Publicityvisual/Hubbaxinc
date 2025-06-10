import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
HF_API_TOKEN = os.getenv('HF_API_TOKEN')
HF_MODEL_URL = os.getenv('HF_MODEL_URL', 'https://api-inference.huggingface.co/models/bigscience/bloomz-560m')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json() or {}
    prompt = data.get('prompt', '')
    headers = {
        'Authorization': f'Bearer {HF_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.post(HF_MODEL_URL, headers=headers, json={'inputs': prompt})
    return jsonify(response.json())

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
