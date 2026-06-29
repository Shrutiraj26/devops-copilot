import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from groq import Groq

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are DevOps Copilot — an expert AI assistant specialized in DevOps, infrastructure, and software engineering.

You help engineers with:
- Debugging error logs and stack traces (Docker, Kubernetes, CI/CD, Linux, Python, Java)
- Writing and explaining Dockerfiles, docker-compose.yml files
- Writing GitHub Actions CI/CD pipeline YAML
- Writing and debugging Kubernetes manifests (Deployments, Services, Ingress, ConfigMaps)
- Explaining shell/bash commands and scripts
- Troubleshooting cloud infrastructure (AWS, GCP, Azure)
- Writing and fixing Terraform and Helm configurations
- Explaining Git errors and workflows

Rules:
- Always format code blocks with the correct language tag (```dockerfile, ```yaml, ```bash, ```python, etc.)
- Be concise but thorough — give the fix first, explanation after
- If given an error log, always identify: Root Cause, Why It Happened, How to Fix It
- If asked to generate config files, produce production-ready output with comments
- If something is ambiguous, ask one clarifying question before proceeding
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    messages = data.get('messages', [])

    if not messages:
        return jsonify({'error': 'No messages provided'}), 400

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
            max_tokens=2048,
            temperature=0.3
        )
        return jsonify({'answer': response.choices[0].message.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5003)
