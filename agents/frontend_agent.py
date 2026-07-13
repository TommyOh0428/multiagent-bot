class FrontendAgent:
    def __init__(self, instructions_file):
        with open(instructions_file, "r") as file:
            self.instructions = file.readlines()

    def process_command(self, command):
        return f"FrontendAgent received: {command}"
