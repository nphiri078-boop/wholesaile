from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests
from groq import Groq

load_dotenv()
app = Flask(__name__)

# Load your secrets safely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
VAPI_API_KEY = os.getenv("VAPI_API_KEY")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "You are Jarvis, your Madera CA wholesale real estate assistant.")

groq_client = Groq(api_key=GROQ_API_KEY)

# Home page to confirm it's running
@app.route("/", methods=["GET"])
def home():
    return "✅ Jarvis Wholesale Assistant is LIVE! Connected to Vapi, Groq, and n8n."

# Receive calls from Vapi and send to n8n
@app.route("/vapi-webhook", methods=["POST"])
def vapi_handler():
    try:
        call_data = request.json
        # Send full call data to your n8n workflow
        n8n_response = requests.post(N8N_WEBHOOK_URL, json=call_data, timeout=10)
        return jsonify({"status": "success", "n8n_received": n8n_response.ok}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Required for Render free hosting
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
