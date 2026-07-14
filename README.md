<h4 align="center">
    <br> <img src="public/discord.png">
</h4>

<h4 align="center">
    Multiagent Discord Bot
    <!-- <div align="center">
    <br>
        <a href=".">
            <img src="https://github.com/sfuosdev/Website/actions/workflows/node.yml/badge.svg"/>
        </a>
    </div> -->
</h4>

<p align="center">
    <a href="#description">Description</a> •
    <a href="#project-structure">Structure</a> •
    <a href="#how-does-it-work">How does it work</a> •
    <a href="#license">License</a> •
    <a href="#setup"> Setup</a>
</p>

### Description

This project is a multi-agent discord bot that simulates a software development team. The bot has four agents: frontend, backend, devops, and scrum master. Each agent has its own set of instructions and can communicate with other agents to complete tasks. Throughout this project, users can interact with the bot to assign tasks to agents, check the status of tasks, and view the instructions for each agent with faster software development.

### Project structure

```txt
├── agents/
│   ├── __init__.py        # Initialize agents module
│   ├── frontend_agent.py  # Frontend agent logic
│   ├── backend_agent.py   # Backend agent logic
│   ├── devops_agent.py    # DevOps agent logic
│   ├── scrum_master_agent.py # Scrum master logic
│   ├── helper.py          # Shared agent helpers
│   └── instructions/
│       ├── frontend.md
│       ├── backend.md
│       ├── devops.md
│       └── scrum-master.md
│
├── tests/
│   ├── test_agents.py     # Unit tests for agent logic
│   ├── test_integration.py # Integration tests
│
├── .env                   # Environment variables (e.g., Discord token) [change .env.example to .env]
├── main.py                # FastAPI Discord webhook
├── Dockerfile             # Cloud Run container
├── deploy.sh              # Cloud Run deployment
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── .gitignore             # Files to ignore in git
└── LICENSE                # Project license
```

### How does it work?

<h4 align="center">
    <br> <img src="public/structure.png">
</h4>

[need to work on more]

prototype

AI Routing

### License

This project is under MIT Licnese. You are welcome to contribute to this project.

### Setup

This project requires virtual environment to manage dependencies.
This project has built with Python 3.11.

#### How to create virtual environment

```bash
# create virtual environment
python3 -m venv venv

# activate virtual environment using shell script
source activate_venv.sh

# install all dependencies
pip install -r requirements.txt
```

#### Run locally

```bash
uvicorn main:app --reload --port 8080
```

Configure Discord's interactions endpoint to the public URL that forwards to
`POST /`. A health check is available at `GET /health`.

#### Deploy to Cloud Run

Authenticate with `gcloud`, then run:

```bash
export GCP_PROJECT_ID="your-project-id"
export GCP_REGION="us-central1" # optional
./deploy.sh
```

Set `DISCORD_PUBLIC_KEY` and `OPENAI_API_KEY` on Cloud Run using Secret Manager
or Cloud Run secret environment variables. Do not put `.env` in the image.
