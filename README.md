# Multiagent discord bot

## Description

## Demo

## How the project structure
```txt
├── agents/
│   ├── __init__.py        # Initialize agents module
│   ├── frontend_agent.py  # Frontend agent logic
│   ├── backend_agent.py   # Backend agent logic
│   ├── devops_agent.py    # DevOps agent logic
│   ├── scrum_master_agent.py # Scrum master logic
│
├── instructions/
│   ├── frontend.txt
│   ├── backend.txt
│   ├── devops.txt
│   ├── scrum-master.txt
│
├── app/
│   ├── __init__.py        # Initialize Flask app
│   ├── routes.py          # Flask routes for inter-agent communication
│
├── bot/
│   ├── __init__.py        # Initialize Discord bot
│   ├── commands.py        # Define Discord bot commands
│
├── tests/
│   ├── test_agents.py     # Unit tests for agent logic
│   ├── test_integration.py # Integration tests
│
├── requirements.txt       # Python dependencies
├── serverless.yml         # Serverless framework config (for AWS Lambda)
├── .env                   # Environment variables (e.g., Discord token)
├── main.py                # Entry point for running locally
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── .gitignore             # Files to ignore in git
└── LICENSE                # Project license
```

### How to create virtual environment

```bash
# create virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# fish shell
. venv/bin/activate.fish
```

### How to install all dependencies

```bash
pip install -r requirements.txt
```
