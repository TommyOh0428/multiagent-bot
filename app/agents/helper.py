def load_instructions(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()