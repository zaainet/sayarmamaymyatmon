from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/api/visual', methods=['POST'])
def get_visual_chart():
    try:
        user_payload = request.json
        
        # Vercel Settings ထဲမှ API Key ကို လှမ်းယူခြင်း
        api_key = os.environ.get("FREE_ASTRO_API_KEY")
        
        headers = {
            "Content-Type": "application/json",
            "x-api-key": api_key
        }
        
        visual_api_url = "https://api.freeastroapi.com/api/v1/synastry/visual"
        
        response = requests.post(visual_api_url, json=user_payload, headers=headers)
        response.raise_for_status()
        
        return jsonify(response.json()), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Vercel အတွက်
def handler(environ, start_response):
    return app(environ, start_response)
