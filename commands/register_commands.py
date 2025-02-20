import argparse
import requests
import yaml
import os
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("TOKEN")
APPLICATION_ID = os.getenv("APPLICATION_ID")
URL = f"https://discord.com/api/v9/applications/{APPLICATION_ID}/commands"

def load_yaml(file_path):
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        exit(1)
    
def register_commands(commands):
    """Register commands to Discord API."""
    headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}

    for command in commands:
        response = requests.post(URL, json=command, headers=headers)
        command_name = command.get("name", "Unknown")

        if response.status_code in [200, 201]:
            print(f"Command '{command_name}' created: {response.status_code}")
        elif response.status_code == 429:
            print(f"Command '{command_name}' ratelimited: {response.status_code}")
        else:
            print(f"Failed to create command '{command_name}': {response.status_code}, {response.text}")

def main():
    parsar = argparse.ArgumentParser(description="Register Discord commands.")
    parsar.add_argument("file", help="Path to the YAML file containing the commands.")
    args = parsar.parse_args()
    commands = load_yaml(args.file)

    if not commands:
        print("No commands found.")
        exit(1)
    
    register_commands(commands)

if __name__ == "__main__":
    main()

# with open("discord_commands.yaml", "r") as file:
#     yaml_content = file.read()

# commands = yaml.safe_load(yaml_content)
# headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}

# # Send the POST request for each command
# try:
#     for command in commands:
#         response = requests.post(URL, json=command, headers=headers)
#         command_name = command["name"]
#         if (response.status_code == 201 or response.status_code == 200):
#             print(f"Command {command_name} created: {response.status_code}")
#         elif response.status_code == 429:
#             print(f"Command {command_name} ratelimited: {response.status_code}")
# except Exception as e:
#     print(f"An error occurred: {e} {response.status_code}")
