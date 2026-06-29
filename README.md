# DevOps Copilot

An AI-powered DevOps assistant built with **LLaMA 3.3 70B** and **Groq** that helps engineers debug error logs, generate infrastructure configs, and troubleshoot pipelines — all in a terminal-themed chat interface.

## What It Can Do

| Task | Example |
|---|---|
| Debug error logs | Paste Docker/K8s/CI/CD errors and get root cause + fix |
| Generate Dockerfiles | Production-ready with multi-stage builds, health checks |
| Write GitHub Actions YAML | Full CI/CD pipelines on demand |
| Fix Kubernetes manifests | Review and correct Deployments, Services, Ingress |
| Explain bash commands | Break down any shell command |
| Generate docker-compose.yml | Multi-service setups with databases and caches |
| AWS CLI help | Explain and fix AWS CLI errors |
| Git error fixes | Diagnose and resolve Git issues |

## Live Demo

**https://devops-copilot-o2ha.onrender.com**

## Demo

```
$ Why is my Docker container exiting with code 137?

> Root Cause: Exit code 137 means the container was killed by the OOM
> (Out of Memory) killer. The container exceeded its memory limit.
>
> How to Fix:
> 1. Increase the memory limit in your docker-compose.yml:
>    mem_limit: 512m
> 2. Or optimize your application's memory usage
> 3. Check current usage with: docker stats <container_id>
```

## Tech Stack

| Category | Tools |
|---|---|
| LLM | LLaMA 3.3 70B via Groq |
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| Syntax Highlighting | highlight.js |
| Markdown Rendering | marked.js |

## Project Structure

```
devops-copilot/
├── app.py              # Flask server + Groq integration
├── requirements.txt
├── .env                # API keys (not committed)
├── .env.example
├── .gitignore
└── templates/
    └── index.html      # Terminal-themed chat UI
```

## Getting Started

```bash
git clone https://github.com/Shrutiraj26/devops-copilot.git
cd devops-copilot
pip install -r requirements.txt
cp .env.example .env   # Add your Groq API key
python app.py
```

Open **http://localhost:5003**

## Get a Free Groq API Key

Sign up at **https://console.groq.com** — no credit card required.
