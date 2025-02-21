import argparse
import time
import requests
import yaml
import os
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("TOKEN")
APPLICATION_ID = os.getenv("APPLICATION_ID")
URL = f"https://discord.com/api/v9/applications/{APPLICATION_ID}/commands"

headers = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json"
}

def delete_all_commands():
    # Fetch all the current global commands that has been created
    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching commands: {response.text}")
        return

    commands = response.json()
    print(f"Found {len(commands)} global commands.")

    # Delete each command with for loop
    for cmd in commands:
        cmd_id = cmd["id"]
        delete_url = f"{URL}/{cmd_id}"
        delete_response = requests.delete(delete_url, headers=headers)
        if delete_response.status_code == 204:
            print(f"Deleted command '{cmd['name']}'")
        else:
            print(f"Failed to delete command '{cmd['name']}': {delete_response.status_code} {delete_response.text}")

if __name__ == "__main__":
    delete_all_commands()