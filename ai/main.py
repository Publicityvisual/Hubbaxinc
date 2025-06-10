import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
HF_API_TOKEN = os.getenv('HF_API_TOKEN')
HF_MODEL_URL = os.getenv(
    'HF_MODEL_URL',
    'https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1'
)

@app.route('/generate', methods=['POST'])
def generate():
    if not HF_API_TOKEN:
        return jsonify({'error': 'HF_API_TOKEN not configured'}), 500

    data = request.get_json() or {}
    prompt = data.get('prompt', '')
    headers = {
        'Authorization': f'Bearer {HF_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(
            HF_MODEL_URL,
            headers=headers,
            json={'inputs': prompt}
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        return jsonify({'error': str(exc)}), 500
    return jsonify(response.json())

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
