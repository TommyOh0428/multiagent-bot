# test_frontend_commands.py
from agents.frontend_agent import FrontendAgent

def test_frontend_process_command(tmp_path):
    instructions_file = tmp_path / "instructions.txt"
    instructions_file.write_text("Instruction line 1\nInstruction line 2")
    
    agent = FrontendAgent(str(instructions_file))
    command = "test command"
    expected_output = f"FrontendAgent received: {command}"
    
    result = agent.process_command(command)
    assert result == expected_output
